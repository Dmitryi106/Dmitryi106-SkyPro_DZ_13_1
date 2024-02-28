from src.product import LawnGrass, Smartphone


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
        Category.total_categories += 1

    # def add_products(self, product):
    #     """
    #     Метод добавляет продукт в категорию
    #     """
    #     self.__products.add(product)
    #     Category.total_products += 1
    #     return self.__products
        def add_products(self, value):
            if not isinstance(value, (Smartphone, LawnGrass)):
                raise TypeError

            elif not issubclass(value.__class__, (Smartphone, LawnGrass)):
                raise TypeError

            else:
                self.__products.append({
                    "name": value[0],
                    "description": value[1],
                    "price": value[2],
                    "quantity": value[3]
                })

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
