class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print(self.products)


s = Shop()
s.add_product("Laptop")
s.add_product("Mobile")
s.list_products()
