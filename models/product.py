class Product:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name

        # State internal
        self._price = price
        self._stock = stock

    @property
    def price(self):
        # Boleh dibaca, tidak boleh ditulis langsung
        return self._price

    @property
    def stock(self):
        return self._stock

    def subtotal(self, quantity):
        return self._price * quantity

    def change_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")

        self._price = new_price

    def reduce_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > self._stock:
            raise ValueError("Insufficient stock")

        self._stock -= quantity
        
    @price.setter
    def price (self, value):
        if value < 0:
            raise ValueError ("Tidak boleh kurang dari 0")
        self ._price = value