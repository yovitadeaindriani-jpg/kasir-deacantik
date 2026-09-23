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

print("--- Masalah Minggu 02 ---") 

indomie = products[0] 

# Di Minggu 02 baris ini mengubah harga menjadi negatif tanpa perlawanan. 
# Sekarang price hanya bisa dibaca, tidak bisa ditulis. 
try:
    indomie.price = -5000
except ValueError as e:
    print("Error:", e)

print() 
print("--- Perubahan lewat method ---") 

indomie.change_price(3500) 
print("Harga baru:", indomie.price) 

indomie.reduce_stock(5) 
print("Stock setelah terjual 5:", indomie.stock)

print() 
print("--- Setiap aturan diuji ---")

try: 
    indomie.change_price(-5000)
except ValueError as error: 
    print("change_price(-5000) ->", error) 

try: 
    indomie.reduce_stock(0) 
except ValueError as error: 
    print("reduce_stock(0) ->", error) 

try: 
    indomie.reduce_stock(-3) 
except ValueError as error: 
    print("reduce_stock(-3) ->", error) 

try: 
    indomie.reduce_stock(999)
except ValueError as error: 
    print("reduce_stock(999) ->", error)
    
try: 
    indomie.reduce_stock(999)
except ValueError as error: 
    print("reduce_stock(999) ->", error) 

print() 
print("Harga akhir:", indomie.price, "| Stock akhir:", indomie.stock) 
print("Percobaan yang gagal tidak mengubah apa pun.")