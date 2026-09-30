"""Model DigitalProduct — Minggu 04 (Inheritance).

Subclass tidak wajib menambah attribute.
Di sini yang berbeda hanya perilakunya.
"""

from models.product import Product


class DigitalProduct(Product):

    def get_description(self):
        return f"{self.name} - Digital Product"

