"""Simple Cashier — Minggu 01 (Foundation). 
Data produk masih disimpan sebagai dictionary biasa. 
Ini DISENGAJA: keterbatasannya akan terasa di Minggu 02, 
dan itulah alasan kita butuh class. 
"""
# Satu produk = satu dictionary.
product = {
    "code": "P001",
    "name": "Indomie",
    "price": 3000,
    "stock": 20,
}
print("Produk pertama:", product["name"])
print()
