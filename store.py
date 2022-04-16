
# will do the functions of storage
class Store:
    def __init__(self):
        self.stock = []

    def add_shoes(self, product, quantity, condition):  # condition  Need to fix that
        if condition:
            self.stock.append((product, quantity))
            print("the condition is {}".format(condition))
        else:
            for (a, b) in self.stock:
                b = (b + quantity)
                print("the condition is {}".format(condition))
        return self.stock

    def add_clothing(self, product, quantity, condition):
        if condition:
            self.stock.append((product, quantity))
        else:
            for (a, b) in self.stock:
                b += quantity
        return self.stock

    def add_condition(self, product):  # Working
        condition = False
        if len(self.stock) > 0:
            for a, b in self.stock:
                if a.name == product:
                    condition = False
                else:
                    condition = True
        if len(self.stock) == 0:
            condition = True
        return condition

    def test_list(self):
        for c, b in self.stock:
            print(c.name, c.price, "we have {} of that product".format(b))
