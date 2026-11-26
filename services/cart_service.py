"""Cart — Minggu 11.

Keranjang belanja: kumpulan CartItem beserta totalnya.
List dipakai di sini, bukan dictionary, karena yang penting adalah
urutan barang dimasukkan — bukan pencarian cepat lewat kunci.
Bandingkan dengan ProductCatalog Minggu 05 yang justru sebaliknya.
"""

from models.cart_item import CartItem

class Cart:
    def __init__(self):
        self.items = []
        
    def add(self, product, quantity):
        self.items.append(CartItem(product, quantity))
        
    def total(self):
        return sum(item.subtotal() for item in self.items)
    
    def is_empty(self):
        return not self.items
    
    def clear(self):
        # Dipakai setelah checkout: keranjang kosong lagi untuk pembeli berikutnya.
        self.items = []