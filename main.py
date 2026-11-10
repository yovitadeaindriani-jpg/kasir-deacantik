
"""Simple Cashier — Minggu 09 (SQLite).

Data produk dibaca dari database SQLite.
Perubahan stok dan transaksi disimpan ke database.
"""

from models.product_catalog import ProductCatalog
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from repositories.database import DATABASE_PATH, create_schema
from services.action_history import ActionHistory
from services.order_queue import OrderQueue
from models.product import Product  # PERBAIKAN: untuk data awal produk


def judul(teks):
    print()
    print("---", teks, "---")


print("=========================")
print("SIMPLE CASHIER")
print("=========================")

# ------------------------------------------------------------------
# Minggu 09 — Persiapan database
# ------------------------------------------------------------------

create_schema()

product_repository = ProductRepository()
order_repository = OrderRepository()

history = ActionHistory()
queue = OrderQueue()

# PERBAIKAN: Isi database dengan produk awal jika masih kosong.
# Data tidak dimasukkan ulang jika database sudah memiliki produk.

if len(product_repository.load()) == 0:
    produk_awal = [
        Product("P001", "Indomie", 3000, 20),
        Product("P002", "Teh Botol", 4000, 15),
        Product("P003", "Teh Kotak", 3500, 10),
        Product("P004", "Roti", 7000, 8),
    ]

    product_repository.save(produk_awal)

# ------------------------------------------------------------------
# Muat produk dari database
# ------------------------------------------------------------------

judul("Muat produk dari database")

products = product_repository.load()

catalog = ProductCatalog()

for product in products:
    catalog.add(product)

print("Sumber data:", DATABASE_PATH)

for product in catalog.all():
    print(
        product.code,
        product.name,
        product.price,
        "stock",
        product.stock
    )

# ------------------------------------------------------------------
# Ambil satu produk: file vs database
# ------------------------------------------------------------------

judul("Ambil satu produk: file vs database")

produk = product_repository.get("P001")
produk_tidak_ada = product_repository.get("P999")

print(
    "repository.get('P001') :",
    produk.name if produk else None
)

print(
    "repository.get('P999') :",
    produk_tidak_ada
)

# ------------------------------------------------------------------
# Struktur data Minggu 05-06 tetap dipakai
# ------------------------------------------------------------------

judul("Struktur data Minggu 05-06 tetap dipakai")

# PERBAIKAN: Cek produk sebelum mengambil atribut name.
produk_teh = catalog.get("P002")

if produk_teh is not None:
    print("catalog.get('P002') :", produk_teh.name)
else:
    print("Produk P002 tidak ditemukan.")

hasil_cari = [
    product.name
    for product in catalog.search("teh")
]

print("catalog.search('teh') :", hasil_cari)

# ------------------------------------------------------------------
# Transaksi lalu simpan ke database
# ------------------------------------------------------------------

judul("Transaksi lalu simpan ke database")

indomie = catalog.get("P001")
jumlah = 3

if indomie is not None:
    print("Stock Indomie sebelum :", indomie.stock)

    if indomie.stock >= jumlah:

        # Aturan bisnis tetap dijaga model, bukan oleh SQL.
        indomie.reduce_stock(jumlah)

        history.push(f"jual Indomie x{jumlah}")

        order = {
            "order_id": order_repository.next_order_id(),
            "total": indomie.subtotal(jumlah),
            "status": "QUEUED",
            "items": [
                {
                    "code": indomie.code,
                    "quantity": jumlah
                }
            ],
        }

        queue.enqueue(order)

        order_repository.save(queue.dequeue())

        product_repository.save(catalog.all())

        print("Stock Indomie sesudah :", indomie.stock)

        print(
            "Order tersimpan :",
            order["order_id"],
            "total",
            order["total"]
        )

    else:
        print("Stock tidak cukup - penjualan dilewati.")

else:
    print("Produk Indomie tidak ditemukan.")

# ------------------------------------------------------------------
# Baca ulang dari koneksi baru
# ------------------------------------------------------------------

judul("Baca ulang dari koneksi baru")

segar = ProductRepository().get("P001")

# PERBAIKAN: Cek agar tidak error jika produk tidak ditemukan.
if segar is not None:
    print("Stock Indomie di database :", segar.stock)
else:
    print("Stock Indomie di database : Produk tidak ditemukan.")

orders = OrderRepository().load()

print("Jumlah order tersimpan :", len(orders))

if orders:
    terakhir = orders[-1]

    print(
        "Order terakhir :",
        terakhir["order_id"],
        terakhir["status"],
        "dengan",
        len(terakhir["items"]),
        "item"
    )

# ------------------------------------------------------------------
# Yang berubah dan yang tetap
# ------------------------------------------------------------------

judul("Yang berubah dan yang tetap")

print("Berubah : repositories/ (CSV/JSON -> SQL)")
print("Tetap : models/, services/ - tidak satu baris pun disentuh")
