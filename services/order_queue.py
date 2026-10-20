
class OrderQueue:
    def __init__(self):
        self.orders = []

    def enqueue(self, order):
        self.orders.append(order)

    def dequeue(self):
        if self.orders:
            return self.orders.pop(0)
        return None

    def is_empty(self):
        return len(self.orders) == 0

    def size(self):
        return len(self.orders)
