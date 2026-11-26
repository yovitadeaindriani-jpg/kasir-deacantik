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


def show_order_queue(order_repository):
    orders = order_repository.load()

    if not orders:
        print("Belum ada order dalam antrean.")
        return

    for order in orders:
        jumlah_item = len(order["items"])
        print(
            f"{order['order_id']:10} {order['status']:8} "
            f"total {order['total']:>7} {jumlah_item} item"
        )

    print(f"\n{len(orders)} order.")


def load_catalog(product_repository):
    catalog = ProductCatalog()

    # Memasukkan produk dari database ke dalam katalog
    for product in product_repository.load():
        catalog.add(product)

    return catalog


def main():
    product_repository = ProductRepository()
    order_repository = OrderRepository()

    catalog = load_catalog(product_repository)

    if not catalog.all():
        print("Database kosong atau belum dibuat.")
        print("Jalankan lebih dulu: python -m scripts.init_db")
        return

    while True:
        show_menu()

        try:
            choice = input("Choose: ").strip()
        except (EOFError, KeyboardInterrupt):
            # Ctrl+D atau Ctrl+C tetap keluar dengan rapi.
            print("\nSampai jumpa.")
            return

        if choice == "1":
            show_products(catalog)

        elif choice == "2":
            search_product(catalog)

        elif choice in ("3", "4", "5"):
            print(BELUM_TERSEDIA)

        elif choice == "6":
            show_order_queue(order_repository)

        elif choice == "0":
            print("Sampai jumpa.")
            return

        else:
            print(f"Pilihan '{choice}' tidak dikenal. Masukkan angka 0-6.")


if __name__ == "__main__":
    main()
