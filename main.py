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
from models.product import Product
from models.food_product import FoodProduct
from models.digital_product import DigitalProduct

PRODUCTS_PATH = "data/products.csv"
ORDERS_PATH = "data/orders.json"
def judul(teks):
    print()
    print("---", teks, "---")
    
print("=========================")
print(" SIMPLE CASHIER")
print(" UTS Checkpoint W01-07")
print("=========================")

# ------------------------------------------------------------------
# Minggu 02-03 — Class, Object, Encapsulation
# ------------------------------------------------------------------
judul("W02-03 Class, Object, Encapsulation")
contoh = Product("P000", "Contoh", 3000, 20)
print("subtotal(2) :", contoh.subtotal(2))
try:
    contoh.price = -5000
except ValueError as e:
    print("Error:", e)
    
try:
    contoh.change_price(-5000)
except ValueError as error:
    print("change_price(-1) :", error)
    
try:
    contoh.reduce_stock(999)
except ValueError as error:
    print("reduce_stock(999):", error)

# ------------------------------------------------------------------
# Minggu 04 — Inheritance & Polymorphism
# ------------------------------------------------------------------
judul("W04 Inheritance & Polymorphism")

varian = [
    Product("P001", "Indomie", 3000, 20),
    FoodProduct("F001", "Roti", 7000, 8, "2026-12-01"),
    DigitalProduct("D001", "E-Book Python", 50000, 99),
]

# Satu loop, tiga hasil berbeda, tanpa memeriksa jenis produk.
for item in varian:
    print(f"{item.code:5} {item.get_description()}")
# ------------------------------------------------------------------
# Minggu 07 — Repository & File (memuat data nyata)
# ------------------------------------------------------------------
judul("W07 Repository & File")

product_repository = ProductRepository(PRODUCTS_PATH)
order_repository = OrderRepository(ORDERS_PATH)

catalog = ProductCatalog()

for product in product_repository.load():
    catalog.add(product)
    
print("Dimuat dari", PRODUCTS_PATH, ":", len(catalog.all()), "produk")
print("File tidak ada :", ProductRepository("data/hilang.csv").load())

# ------------------------------------------------------------------
# Minggu 05 — List & Dictionary
# ------------------------------------------------------------------
judul("W05 Catalog: List & Dictionary")

for item in catalog.all():
    print(f"{item.code:5} {item.name:12} {item.price:>6} stock {item.stock}")
    
print()
print("get('P001') :", catalog.get("P001").name, "(dictionary, satu langkah)")
print("get('P999') :", catalog.get("P999"), "(tidak error)")
print("search('teh') :", [p.name for p in catalog.search("teh")])
print("search('TEH') :", [p.name for p in catalog.search("TEH")])
print("search('kopi') :", catalog.search("kopi"), "(tidak ditemukan)")

# ------------------------------------------------------------------
# Minggu 06 — Stack & Queue
# ------------------------------------------------------------------
judul("W06 Queue (FIFO) vs Stack (LIFO)")

queue = OrderQueue()
history = ActionHistory()

for penanda in ["A", "B", "C"]:
    queue.enqueue(penanda)
    history.push(penanda)
    
print("Masuk : A B C")
print("Queue keluar :", queue.dequeue(), queue.dequeue(), queue.dequeue(), "(FIFO)")
print("Stack keluar :", history.actions.pop(), history.actions.pop(), history.actions.pop(), "(LIFO)")
print("Queue kosong :", queue.dequeue(), "| Stack kosong:", history.pop())