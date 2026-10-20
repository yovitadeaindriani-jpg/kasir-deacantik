"""Simple Cashier — Minggu 07 (File Handling & Persistence).

Produk tidak lagi ditulis di dalam kode.
Data dibaca dari data/products.csv saat program mulai,
dan ditulis kembali saat ada perubahan.
"""

from models.product_catalog import ProductCatalog
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from services.action_history import ActionHistory
from services.order_queue import OrderQueue

PRODUCTS_PATH = "data/products.csv"
ORDERS_PATH = "data/orders.json"

product_repository = ProductRepository(PRODUCTS_PATH)
order_repository = OrderRepository(ORDERS_PATH)

print("=========================")
print("     SIMPLE CASHIER")
print("=========================")
print()

print("--- Muat produk dari CSV ---")

catalog = ProductCatalog()

for product in product_repository.load():
    catalog.add(product)

for item in catalog.all():
    print(item.code, "|", item.name, "| harga", item.price, "| stock", item.stock)

print()
print("--- File tidak ada ---")

kosong = ProductRepository("data/tidak_ada.csv")
print("load() ->", kosong.load(), "(FileNotFoundError ditangani)")

print()
print("--- Transaksi lalu simpan ---")

indomie = catalog.get("P001")
history = ActionHistory()
queue = OrderQueue()

orders = order_repository.load()
jumlah = 3

print("Stock Indomie sebelum:", indomie.stock)

# Penjualan hanya diproses jika stok masih mencukupi.
if indomie.stock >= jumlah:
    indomie.reduce_stock(jumlah)
    history.push(f"jual Indomie x{jumlah}")

    queue.enqueue(f"ORD-{len(orders) + 1:03d} Indomie x{jumlah}")
    orders.append(queue.dequeue())

    product_repository.save(catalog.all())
    order_repository.save(orders)

    print("Stock Indomie sesudah:", indomie.stock)
    print("Perubahan ditulis ke", PRODUCTS_PATH, "dan", ORDERS_PATH)
else:
    print("Stock Indomie tinggal", indomie.stock, "- penjualan dilewati.")
    print("Isi ulang stock di", PRODUCTS_PATH, "untuk mencoba lagi.")

print()
print("--- Baca ulang dari file ---")

# Membaca ulang data seolah-olah program baru dijalankan.
segar = ProductRepository(PRODUCTS_PATH).load()
indomie_lagi = [p for p in segar if p.code == "P001"][0]

print("Stock Indomie setelah dibaca ulang:", indomie_lagi.stock)
print("Order tersimpan:", OrderRepository(ORDERS_PATH).load())

print()
print("--- Mengapa CSV dan JSON? ---")
print("Produk berbentuk tabel datar         -> CSV.")
print("Order berisi daftar item di dalamnya -> JSON.")