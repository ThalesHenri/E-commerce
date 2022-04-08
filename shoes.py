from product import Product


class Shoes(Product):
    def __init__(self, name, weight, price, size):
        super().__init__(name, weight, price)
        self.size = int(size)
