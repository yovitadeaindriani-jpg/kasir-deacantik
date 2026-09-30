"""Model FoodProduct — Minggu 04 (Inheritance).

Produk makanan adalah Product, ditambah satu hal:
tanggal kedaluwarsa.
"""

from models.product import Product


class FoodProduct(Product):
    def __init__(self, code, name, price, stock, expiry_date):
        # super() memanggil __init__ milik Product,
        # sehingga encapsulation Minggu 03 tetap berlaku.
        super().__init__(code, name, price, stock)

        self.expiry_date = expiry_date

    def get_description(self):
        return f"{self.name} - Expired: {self.expiry_date}"

