
"""OrderRepository — Minggu 09 (SQLite).

Order disimpan dalam dua tabel: orders dan order_items.
Di Minggu 07 struktur bersarang ini ditangani JSON; sekarang
dinyatakan sebagai relasi antar tabel.

Order masih berbentuk dictionary sederhana:


    {
        "order_id": "ORD-001",
        "total": 9000,
        "status": "QUEUED",
        "items": [{"code": "P001", "quantity": 3}],
    }
    
Class Order dibuat di Minggu 11.
"""

import sqlite3

from repositories.database import DATABASE_PATH, get_connection

class OrderRepository:
    def __init__(self, path=DATABASE_PATH):
        self.path = path

    def load(self):
        if not self.path.exists():
            return []

        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, orders):
        self.path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(orders, file, indent=4)
            
    def save(self, order):
        """Simpan satu order beserta seluruh itemnya.
        Keduanya ditulis dalam satu transaksi: bila penulisan item gagal,
        order-nya pun tidak jadi tersimpan. Tidak ada order tanpa item.
        """
        
        with get_connection(self.path) as connection:
            connection.execute(
                "INSERT INTO orders (order_id, total, status) VALUES (?, ?, ?)",
                (order["order_id"], order["total"], order["status"]),
            )
            
            for item in order["items"]:
                connection.execute(
                    """
                    INSERT INTO order_items (order_id, code, quantity)
                    VALUES (?, ?, ?)
                    """,
                    (order["order_id"], item["code"], item["quantity"]),
                )
                
    def next_order_id(self):
        with get_connection(self.path) as connection:
            row = connection.execute("SELECT COUNT(*) AS n FROM orders").fetchone()
            
        return f"ORD-{row['n'] + 1:03d}"