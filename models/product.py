class Product:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock
        
    def subtotal (self, quantity):
        return self.price * quantity
