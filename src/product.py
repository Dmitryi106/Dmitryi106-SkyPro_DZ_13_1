class Product:
    products_list = []

    def __init__(self, name, description, price: float, count: int):
        """
        Конструктор класса Product
        """
        self.name = name
        self.description = description
        self._price = price
        self.count = count
        Product.products_list.append(self)

    @classmethod
    def create_product(cls, product_dictionary):
        """
        Метод для создания экземпляра класса Product если подается для дынных словарь
        """
        name = product_dictionary['name']
        description = product_dictionary['description']
        price = product_dictionary['price']
        count = product_dictionary['count']
        for product in cls.products_list:
            if name == product.name:
                product.count += count
                return product

        return cls(name, description, price, count)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: int):
        """Доработать изменение цены!!!!!!!!!!!!"""
        """
        Метод изменения цены
        """
        if value <= 0:
            print('Введена некорректная цена')
        else:
            if self._price > value:
                self._price = value
            elif value < self._price:
                answer = input('Вы уверены, что хотите поменять цену?(y/n)')
                if answer == 'y':
                    self._price = value
                    print(f'Цена изменена на {self._price} руб.')
                elif answer == 'n':
                    print(f'Действие отменено')

    def __str__(self):
        """
        Магический метод выводит продукт, цену, остаток на складе
        """
        return f'{self.name}, {self.price} руб. Остаток: {self.count} шт'

    def __add__(self, other):
        """
        Магический метод считает общую стоимость продуктов и количество шт. на складе
        """
        return f'{self.price * self.count + other.price * other.count} руб. общая цена всех продуктов на складе.\nОбщее количество продуктов {self.count + other.count} шт на склад'
