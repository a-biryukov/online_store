class Base:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Category(Base):
    def __init__(self, name, description, products):
        super().__init__(name, description)
        self.products = products


class Product(Base):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description)
        self.price = price
        self.quantity = quantity
