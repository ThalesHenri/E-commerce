

# will do the functions of storage
class Store:
    def __init__(self):
        self.stock = []

    def add_shoes(self, product, quantity):  # condition):
        """if condition is True:
            self.stock.append((product, quantity))
        if condition is False:
            for a, b in self.stock:
                b = (b + quantity)

    def add_condition(self, product):
        condition = False
        if len(self.stock) == 0:
            for a, b in self.stock:
                if not a.name == product.name:
                    condition = True
                else:
                    condition = False
        return condition"""
        self.stock.append((product, quantity))

    def test_list(self):
        for (c, b) in self.stock:
            print(c.name, c.price, "we have {} of that product".format(b))
