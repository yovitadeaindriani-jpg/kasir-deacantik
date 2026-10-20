
import csv
from pathlib import Path

from models.product import Product
from models.food_product import FoodProduct
from models.digital_product import DigitalProduct


class ProductRepository:
    def __init__(self, path):
        self.path = Path(path)

    def load(self):
        products = []

        if not self.path.exists():
            return products

        with open(self.path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                code = row["code"]
                name = row["name"]
                price = int(row["price"])
                stock = int(row["stock"])

                if code.startswith("F"):
                    expiry_date = row.get("expiry_date", "")
                    product = FoodProduct(
                        code, name, price, stock, expiry_date
                    )
                elif code.startswith("D"):
                    product = DigitalProduct(code, name, price, stock)
                else:
                    product = Product(code, name, price, stock)

                products.append(product)

        return products

    def save(self, products):
        self.path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.path, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["code", "name", "price", "stock", "expiry_date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()

            for product in products:
                writer.writerow({
                    "code": product.code,
                    "name": product.name,
                    "price": product.price,
                    "stock": product.stock,
                    "expiry_date": getattr(product, "expiry_date", "")
                })
