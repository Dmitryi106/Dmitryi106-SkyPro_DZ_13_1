class Category:

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products):
        """
        Конструктор класса Category
        """
        self.name = name
        self.description = description
        self.__products = set(products)



    def add_products(self, product):
        """
        Метод добавляет продукт в категорию
        """
        self.__products.add(product)
        Category.total_categories += 1
        return self.__products

    @property
    def products(self):
        """
        Метод возвращает список продуктов с полной информацией
        """
        info_list = []
        for product in self.__products:
            info_list.append(f'{product.name}, {product.price} руб. Остаток: {product.count} шт')
        return info_list


    def __str__(self):
        """
        Метод выводит в виде строки категорию продукта и его количество
        """
        return f'{self.name}, количество продуктов {len(self)} шт'


    def __len__(self):
        """
        Метод вычисляет общее количество товара на складе
        """
        count_all_products = 0
        for product in self.__products:
            count_all_products += product.count
        return count_all_products



