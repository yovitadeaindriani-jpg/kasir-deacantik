"""ProductRepository — Minggu 09 (SQLite).

Sumber datanya berganti dari CSV menjadi database.
Interface load() dan save() sengaja tidak berubah, sehingga
Product, ProductCatalog, dan seluruh service tidak perlu disentuh.
"""

import sqlite3

from models.product import Product
from repositories.database import DATABASE_PATH, get_connection


class ProductRepository:
    def __init__(self, path=DATABASE_PATH):
        self.path = path
        
    def load(self):
        products = []
        
        try:
            with get_connection(self.path) as connection:
                rows = connection.execute(
                    "SELECT code, name, price, stock FROM products"
                ).fetchall()
        except sqlite3.OperationalError:
            # Tabel belum ada. Sama semangatnya dengan FileNotFoundError
            # di Minggu 07: program tetap jalan dengan data kosong.
            return []
        
        for row in rows:
            # Kolom INTEGER sudah bertipe int, tidak perlu int() manual
            # seperti pada csv.DictReader.
            products.append(
                Product(row["code"], row["name"], row["price"], row["stock"])
            )
        return products

    def save(self, products):
        with get_connection(self.path) as connection:
            for product in products:
                # Tanda ? adalah parameterized query.
                # Nilai dikirim terpisah dari perintah SQL-nya,
                # sehingga isi data tidak pernah dibaca sebagai perintah.
                connection.execute(
                    """
                    INSERT OR REPLACE INTO products (code, name, price, stock)
                    VALUES (?, ?, ?, ?)
                    """,
                    (product.code, product.name, product.price, product.stock),
                )
                
    def get(self, code):
        """Ambil satu produk langsung dari database.
        Di Minggu 07 ini berarti membaca seluruh file lebih dulu.
        """
        
        with get_connection(self.path) as connection:
            row = connection.execute(
                "SELECT code, name, price, stock FROM products WHERE code = ?",
                (code,),
                ).fetchone()
            
        if row is None:
            return None
        return Product(row["code"], row["name"], row["price"], row["stock"])
