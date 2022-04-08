from product import Product
""" the diferrence btwn theese child class are the size,
one will be int like the number of the shoes you were,
and the other will be a str like XG, G, M P """


class Clothing(Product):
    def __init__(self, name, weight, price, size):
        super().__init__(name, weight, price)
        self.size = size
