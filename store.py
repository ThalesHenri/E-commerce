from product import Product
from clothing import Clothing
from shoes import Shoes

# will do the functions of storage
class Store:
    def __init__(self):
        self.stock = []

    def add_shoes(self, product, quantity):
        self.stock.append((product, quantity))

    def test_list(self):
        for c, b in self.stock:
            print(c.name, c.price, "we have {} of that product".format(b))
