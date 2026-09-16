from models.product import Product

product = Product("P001", "Indomie", 3000, 20)
print("Produk pertama:", product.name)
print("Subtotal 2 Indomie =", product.subtotal(2))
print()

products = [
    Product("P001", "Indomie", 3000, 20),
    Product("P002", "Teh Botol", 4000, 15),
    Product("P003", "Roti", 7000, 8),
]

print("=========================")
print("     SIMPLE CASHIER")
print("=========================")
print()

for item in products:
    print(item.code, item.name, item.price, item.stock)

print()

print("--- Minggu 01 vs Minggu 02 ---")

# Minggu 01 — dictionary.
product_dict = {"code": "P001", "name": "Indomie", "price": 3000, "stock": 20}
print("dictionary :", product_dict["name"], "subtotal",
      product_dict["price"] * 2)

# Minggu 02 — object. Rumus subtotal tidak lagi ditulis ulang di sini.
print("object     :", product.name, "subtotal", product.subtotal(2))

print()
print("--- Catatan untuk Minggu 03 ---")

# Satu masalah Minggu 01 sudah selesai: perilaku kini menyatu dengan data.
# Tetapi datanya masih belum terjaga.
products[0].price = -5000
products[0].stock = -100
print("Harga sekarang:", products[0].price, "(negatif, masih diterima)")
print("Stock sekarang:", products[0].stock, "(negatif, masih diterima)")
print("Belum ada yang menjaga aturan ini -> encapsulation di Minggu 03.")
