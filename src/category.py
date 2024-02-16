class Category:
    name: str
    description: str
    products: list

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = str(name)
        self.description = str(description)
        self.products = list(products)
        Category.total_categories += 1
        Category.total_products += len(self.products)


    def products(self, product):
        self.products.append(product)


    def __str__(self):
        return f'{self.products[0]}, {self.products[2]} руб. Остаток: {self.products[3]} шт'






category = Category("Видеокарты", "игровые видеокарты для компьютера", ["MSI NVIDIA GeForce RTX 4060TI", "видеопамять 8Gb", 59000, 15])
print(category)
print(category.products)
category = Category("Видеокарты", "игровые видеокарты для компьютера", ["MSI NVIDIA GeForce RTX 4060", "видеопамять 6Gb", 40000, 25])
print(category)
print(category.products)