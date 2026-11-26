"""CartItem — Minggu 11.

Satu baris dalam keranjang: produk apa, berapa banyak.
Quantity disimpan di sini, bukan di Product, karena jumlah yang dibeli
adalah milik transaksi — bukan sifat produknya. Produk yang sama bisa
muncul dengan quantity berbeda di keranjang pembeli lain.
"""

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        
    def subtotal(self):
        # Harga tetap ditanyakan ke produknya, tidak disalin ke sini.
        return self.product.subtotal(self.quantity)