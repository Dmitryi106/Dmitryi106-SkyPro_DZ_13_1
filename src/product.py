class Product:
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name, description, price, quantity):
        self.name = str(name)
        self.description = str(description)
        self._price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт'


    @classmethod
    def new_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)


    @property
    def price(self):
        return self._price


    @price.setter
    def price(self, value):
        if value <= 0:
            print('Введена некорректная цена')
        else:
            self._price = value


product = Product("MSI NVIDIA GeForce RTX 4060TI", "видеопамять 8Gb", 59000, 15)
print(str(product))

