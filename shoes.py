from product import Product



class Shoes(Product):
    def __init__(self, name, weight, quantity, size):
        super().__init__(name, weight, quantity)
        self.size = int(size)
