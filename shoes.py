import product


class Shoes(product):
    def __init__(self, name, weight, quantity, size):
        super().__init__(name, weight, quantity)
        self.size = int(size)
