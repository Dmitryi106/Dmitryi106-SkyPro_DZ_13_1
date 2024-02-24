class Category:
    name: str
    description: str
    __products: list

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        self.name = str(name)
        self.description = str(description)
        self.__products = list(products)
        Category.total_categories += 1
        Category.total_products += len(self.__products)


    @property
    def products(self):
        return f'{self.__products[0]}, {self.__products[2]} руб. Остаток: {self.__products[3]} шт'


    @products.setter
    def products(self, product):
        self.__products.append(product)


# category = Category("Видеокарты", "игровые видеокарты для компьютера", ["MSI NVIDIA GeForce RTX 4060TI", "видеопамять 8Gb, Тип видеопамяти GDDR6, Частота видеопамяти 18000 МГц", 59000, 10])
# print(category.products)
# category.products("MSI NVIDIA Ge")
# print(category.products)
# category.products('radeon AMD 21080')
# print(category.products)
#
# category = Category("Видеокарты", "игровые видеокарты для компьютера", ["MSI NVIDIA GeForce RTX 4060TI", "видеопамять 8Gb, Тип видеопамяти GDDR6, Частота видеопамяти 18000 МГц", 59000, 10])
# print(category.print_products)

