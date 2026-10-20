
import json
from pathlib import Path


class OrderRepository:
    def __init__(self, path):
        self.path = Path(path)

    def load(self):
        if not self.path.exists():
            return []

        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, orders):
        self.path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(orders, file, indent=4)
