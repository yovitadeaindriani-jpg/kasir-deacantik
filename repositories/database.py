"""Koneksi database — Minggu 09.

Satu-satunya tempat yang tahu bahwa databasenya kebetulan SQLite.
"""

import sqlite3
DATABASE_PATH = "data/cashier.db"
SCHEMA_PATH = "data/schema.sql"

def get_connection(path=DATABASE_PATH):
    connection = sqlite3.connect(path)
    
    # Hasil query dapat diakses seperti dictionary: row["name"].
    # Alurnya sama dengan csv.DictReader di Minggu 07.
    connection.row_factory = sqlite3.Row
    
    # SQLite tidak menegakkan FOREIGN KEY kecuali diminta.
    connection.execute("PRAGMA foreign_keys = ON")
    
    return connection

def create_schema(path=DATABASE_PATH, schema_path=SCHEMA_PATH):
    with open(schema_path) as file:
        schema = file.read()
        
    with get_connection(path) as connection:
        connection.executescript(schema)