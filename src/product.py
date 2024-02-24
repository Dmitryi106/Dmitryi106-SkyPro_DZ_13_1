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


# product = Product("MSI NVIDIA GeForce RTX 4060TI", "видеопамять 8Gb, Тип видеопамяти GDDR6, Частота видеопамяти 18000 МГц", 59000, 10)
#
# Product.new_product("MSI NVIDIA GeForce RTX 4060TI", "видеопамять 8Gb, Тип видеопамяти GDDR6, Частота видеопамяти 18000 МГц", 59000, 10)

