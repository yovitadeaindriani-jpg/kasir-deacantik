"""Bangun database dari skema, lalu isi dengan data awal — Minggu 09.

Jalankan:
python -m scripts.init_db

Aman dijalankan berulang: skema memakai CREATE TABLE IF NOT EXISTS
dan produk dimasukkan dengan INSERT OR IGNORE, sehingga stock yang
sudah berubah tidak ditimpa kembali.
"""

import csv

from repositories.database import DATABASE_PATH, create_schema, get_connection

PRODUCTS_CSV = "data/products.csv"

def migrate_products(path=DATABASE_PATH, csv_path=PRODUCTS_CSV):
    """Pindahkan data contoh dari CSV ke tabel products.
    Data tidak diketik ulang. CSV Minggu 07 tetap menjadi sumber awalnya.
    """
    with open(csv_path, newline="") as file:
        rows = list(csv.DictReader(file))
        
    with get_connection(path) as connection:
        for row in rows:
            
            connection.execute(
                """
                INSERT OR IGNORE INTO products (code, name, price, stock)
                VALUES (?, ?, ?, ?)
                """,
                (row["code"], row["name"], int(row["price"]), int(row["stock"])),
            )
    return len(rows)

def main():
    create_schema()
    print("Skema dibuat dari data/schema.sql")
    
    jumlah = migrate_products()
    print(f"{jumlah} produk dimigrasikan dari {PRODUCTS_CSV}")
    
    with get_connection() as connection:
        total = connection.execute("SELECT COUNT(*) AS n FROM products").fetchone()
        print(f"Total produk di database: {total['n']}")
        
    print(f"Database siap: {DATABASE_PATH}")
    
    
if __name__ == "__main__":
    main()