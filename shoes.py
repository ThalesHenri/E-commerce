from product import Product



class Shoes(Product):
    def __init__(self, name, weight, quantity, size, price):
        super().__init__(name, weight, quantity, price)
        self.size = int(size)
