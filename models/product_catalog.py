"""ProductCatalog — Minggu 05 (Dictionary).
Katalog menyimpan produk dalam dictionary yang di-index oleh code.
Alasannya: pencarian berdasarkan code adalah operasi paling sering
dipakai kasir, dan dictionary melakukannya dalam satu langkah.
"""
class ProductCatalog:
    def __init__(self):
      # key = code produk, value = object Product
      self.products = {}
      
    def add(self, product):
      self.products[product.code] = product
      
    def get(self, code):
       # .get() mengembalikan None bila code tidak ada,
       # bukan melempar KeyError.
       return self.products.get(code)
   
    def remove(self, code):
       # Argumen kedua membuat penghapusan code yang tidak ada
       # tidak menjatuhkan program.
       self.products.pop(code, None)
    def all(self):
       # List, karena untuk ditampilkan yang penting urutannya.
       return list(self.products.values())
   
