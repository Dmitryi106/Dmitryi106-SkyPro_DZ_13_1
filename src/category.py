class Category:
    name: str
    description: str
    products: list

    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = str(name)
        self.description = str(description)
        self.products = list(products)
        Category.total_categories += 1
        Category.total_products += len(self.products)