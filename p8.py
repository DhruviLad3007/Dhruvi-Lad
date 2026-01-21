class Laptop:
    def __init__(self, price):
        self.price = price

    def apply_discount(self, percent):
        self.price -= self.price * percent / 100


l = Laptop(60000)
l.apply_discount(10)
print("Final Price:", l.price)
