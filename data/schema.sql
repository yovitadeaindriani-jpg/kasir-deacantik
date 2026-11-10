-- Skema database Simple Cashier — Minggu 09
--
-- File ini yang di-commit, bukan file .db-nya.
-- Database dapat dibangun ulang kapan saja dari skema + data awal.
CREATE TABLE IF NOT EXISTS products (
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    stock INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    total INTEGER NOT NULL,
    status TEXT NOT NULL
);

-- Satu order berisi banyak item.
-- Bentuk bersarang yang di Minggu 07 ditangani JSON,
-- di database dinyatakan lewat tabel terpisah + FOREIGN KEY.
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id TEXT NOT NULL,
    code TEXT NOT NULL,
    quantity INTEGER NOT NULL,
FOREIGN KEY (order_id) REFERENCES orders(order_id)
);