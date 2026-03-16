class ProductModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_product_info(self):
        return f"Product Name: {self.name}, Price {self.price}"
