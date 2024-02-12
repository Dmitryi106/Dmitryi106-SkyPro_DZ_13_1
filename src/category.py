class Category:
    name: str
    description: str
    _products: list

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = str(name)
        self.description = str(description)
        self._products = list(products)
        Category.total_categories += 1
        Category.total_products += len(self._products)

    @property
    def get_products(self):
        return self._products

    def get_products(self):
        for product in self._products:
            print(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")

    def add_product(self, product):
        self._products.append(product)


category = Category("Видеокарты", "игровые видеокарты для компьютера", ["MSI NVIDIA GeForce RTX 4060TI", "MSI NVIDIA GeForce RTX 4070Ti"])
print()
# category = Category("Видеокарты", "игровые видеокарты для компьютера", ["MSI NVIDIA GeForce RTX 4060TI", "MSI NVIDIA GeForce RTX 4070Ti"])
# print(category.get_products)
# category.add_product("MSI NVIDIA Ge")
# print(category.get_products)
