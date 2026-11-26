from models.product_catalog import ProductCatalog
from repositories.order_repository import OrderRepository
from repositories.product_repository import ProductRepository
from repositories.database import DATABASE_PATH, create_schema
from services.action_history import ActionHistory
from services.order_queue import OrderQueue
from models.product import Product  # PERBAIKAN: untuk data awal produk
from models.order import Order
from services.cart_service import Cart

def judul(teks):
    print()
    print("---", teks, "---")


MENU = """
=========================
    SIMPLE CASHIER
=========================

1. Product List
2. Search Product
3. Add to Cart
4. View Cart
5. Checkout
6. Order Queue
0. Exit
"""


BELUM_TERSEDIA = "Belum tersedia. Menu ini diaktifkan pada Minggu 11."


def show_menu():
    print(MENU)


def format_product(product):
    return f"{product.code:6} {product.name:15} {product.price:>7} {product.stock:>6}"


def show_header():
    print(f"{'CODE':6} {'NAME':15} {'PRICE':>7} {'STOCK':>6}")
    print("-" * 37)


def show_products(catalog):
    products = catalog.all()

    if not products:
        print("Katalog kosong.")
        return

    show_header()

    for product in products:
        print(format_product(product))


# FUNGSI YANG DITAMBAHKAN
def load_catalog(product_repository):
    """Memuat produk dari database ke ProductCatalog."""

    catalog = ProductCatalog()
    products = product_repository.load()

    for product in products:
        catalog.add(product)

    return catalog


# FUNGSI YANG DITAMBAHKAN
def show_order_queue(order_repository):
    """Menampilkan order yang tersimpan di database."""

    orders = order_repository.load()

    if not orders:
        print("Belum ada order.")
        return

    print("\n=== ORDER QUEUE ===")

    for order in orders:
        print(f"\nOrder ID : {order['order_id']}")
        print(f"Status   : {order['status']}")
        print(f"Total    : Rp{order['total']:,}")

        print("Item:")
        for item in order["items"]:
            print(f"  - {item['code']} x{item['quantity']}")


def search_product(catalog):
    keyword = input("Kata kunci: ").strip()

    if not keyword:
        print("Kata kunci kosong.")
        return

    results = catalog.search(keyword)

    if not results:
        print(f"Tidak ada produk yang cocok dengan '{keyword}'.")
        return

    show_header()

    for product in results:
        print(format_product(product))


def add_to_cart(catalog, cart):
    code = input("Kode produk: ").strip().upper()
    product = catalog.get(code)
    
    if product is None:
        print(f"Produk '{code}' tidak ditemukan.")
        return
    
    # int() masih polos di sini. Input bukan angka akan menghentikan program,
    # dan itulah masalah yang diselesaikan Minggu 12.
    quantity = int(input("Jumlah: ").strip())
    
    if quantity <= 0:
        print("Jumlah harus lebih besar dari nol.")
        return
    
    cart.add(product, quantity)
    print(f"{product.name} x{quantity} masuk keranjang.")


def view_cart(cart):
    if cart.is_empty():
        print("Keranjang masih kosong.")
        return
    
    print(f"{'NAME':15} {'QTY':>4} {'SUBTOTAL':>10}")
    print("-" * 31)
    
    for item in cart.items:
        print(f"{item.product.name:15} {item.quantity:>4} {item.subtotal():>10}")
    print("-" * 31)
    print(f"{'TOTAL':15} {'':>4} {cart.total():>10}")


def checkout(cart, catalog, product_repository, order_repository, queue):
    if cart.is_empty():
        print("Keranjang masih kosong. Tidak ada yang bisa di-checkout.")
        return

    # Periksa seluruh item lebih dulu, baru ubah apa pun.
    # Tanpa ini, kegagalan pada item ketiga akan menyisakan stock
    # item pertama dan kedua yang sudah terlanjur berkurang.
    for item in cart.items:
        if item.quantity > item.product.stock:
            print(
                f"Checkout dibatalkan: {item.product.name} - "
                f"stock {item.product.stock}, diminta {item.quantity}."
            )
            return

    # Baru sekarang state diubah, lewat model — bukan assignment langsung.
    for item in cart.items:
        item.product.reduce_stock(item.quantity)

    order = Order(
        order_repository.next_order_id(),
        list(cart.items),
        cart.total(),
    )

    queue.enqueue(order)
    order_repository.save(queue.dequeue())

    product_repository.save(catalog.all())

    print(f"Order {order.order_id} dibuat. Total {order.total}.")
    print(f"{order.item_count()} item masuk antrean.")

    cart.clear() 
    
def main():
    # Inisialisasi database
    create_schema()

    product_repository = ProductRepository()
    order_repository = OrderRepository()

    catalog = load_catalog(product_repository)

    # Inisialisasi keranjang dan antrean
    cart = Cart()
    queue = OrderQueue()

    while True:
        show_menu()
        choice = input("Pilih menu: ").strip()

        if choice == "1":
            show_products(catalog)
        elif choice == "2":
            search_product(catalog)
        elif choice == "3":
            add_to_cart(catalog, cart)
        elif choice == "4":
            view_cart(cart)
        elif choice == "5":
            checkout(cart, catalog, product_repository, order_repository, queue)
        elif choice == "6":
            show_order_queue(order_repository)
        elif choice == "0":
            print("Sampai jumpa.")
            return
        else:
            print(f"Pilihan '{choice}' tidak dikenal. Masukkan angka 0-6.")


if __name__ == "__main__":
    main()