
"""OrderRepository — Minggu 09 (SQLite).

Order disimpan dalam dua tabel: orders dan order_items.
Di Minggu 07 struktur bersarang ini ditangani JSON; sekarang
dinyatakan sebagai relasi antar tabel.

Order masih berbentuk dictionary sederhana.
Class Order dibuat di Minggu 11.
"""

from repositories.database import DATABASE_PATH, get_connection


class OrderRepository:
    def __init__(self, path=DATABASE_PATH):
        self.path = path

    def load(self):
        """Baca semua order beserta itemnya dari database."""

        orders = []

        with get_connection(self.path) as connection:
            rows = connection.execute(
                """
                SELECT order_id, total, status
                FROM orders
                ORDER BY rowid
                """
            ).fetchall()

            for row in rows:
                items = connection.execute(
                    """
                    SELECT code, quantity
                    FROM order_items
                    WHERE order_id = ?
                    """,
                    (row["order_id"],),
                ).fetchall()

                orders.append({
                    "order_id": row["order_id"],
                    "total": row["total"],
                    "status": row["status"],
                    "items": [
                        {
                            "code": item["code"],
                            "quantity": item["quantity"]
                        }
                        for item in items
                    ],
                })

        return orders

    def save(self, order):
        """Simpan satu order beserta seluruh itemnya."""

        with get_connection(self.path) as connection:
            connection.execute(
                """
                INSERT INTO orders (order_id, total, status)
                VALUES (?, ?, ?)
                """,
                (
                    order["order_id"],
                    order["total"],
                    order["status"],
                ),
            )

            for item in order["items"]:
                connection.execute(
                    """
                    INSERT INTO order_items (order_id, code, quantity)
                    VALUES (?, ?, ?)
                    """,
                    (
                        order["order_id"],
                        item["code"],
                        item["quantity"],
                    ),
                )

    def next_order_id(self):
        with get_connection(self.path) as connection:
            row = connection.execute(
                "SELECT COUNT(*) AS n FROM orders"
            ).fetchone()

        return f"ORD-{row['n'] + 1:03d}"
