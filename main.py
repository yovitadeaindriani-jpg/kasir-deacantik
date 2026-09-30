from models.product import Product
from models.food_product import FoodProduct
from models.digital_product import DigitalProduct

products = [
    Product("P001", "Indomie", 3000, 20),
    FoodProduct("F001", "Roti", 7000, 8, "2026-12-01"),
    DigitalProduct("D001", "E-Book Python", 50000, 99),
]


print("=========================")
print("     SIMPLE CASHIER")
print("=========================")
print()

print("--- Polymorphism ---")

# Satu list berisi tiga jenis object,
# satu loop, tiga hasil berbeda.
# main.py tidak perlu tahu jenis produknya.

for item in products:
    print(item.code, "|", item.get_description())

print()

print("--- Yang diwarisi dari Product ---")

roti = products[1]

# subtotal() tidak ditulis ulang di FoodProduct,
# tetapi tetap bisa dipakai.
print("Subtotal 3 Roti:", roti.subtotal(3))

# expiry_date hanya dimiliki FoodProduct.
print("Kedaluwarsa Roti:", roti.expiry_date)


print()

print("--- Encapsulation Minggu 03 tetap berlaku di subclass ---")

try:
    roti.price = 1
except AttributeError:
    print("FoodProduct.price tetap read-only.")

try:
    roti.change_price(-1000)
except ValueError as error:
    print("FoodProduct.change_price(-1000) ->", error)

try:
    roti.reduce_stock(999)
except ValueError as error:
    print("FoodProduct.reduce_stock(999) ->", error)

roti.reduce_stock(3)
print("Stock Roti setelah terjual 3:", roti.stock)

print()

print("Aturan ditulis sekali di Product, dipakai semua turunannya.")

