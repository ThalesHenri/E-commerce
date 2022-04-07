from product import Product
from clothing import Clothing
from shoes import Shoes


class Store:
    def __init__(self):
        self.stock = []


    def add_shoes(self, product):
        """products = [product.name, product.weight, product.quantity,
        product.size, product.price]"""
        self.stock.append(product)

    def test_list(self):
        for c in self.stock:
        	print(c.name)
        	print(c.price)
