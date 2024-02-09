class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = str(name)
        self.description = str(description)
        self.price = float(price)
        self.quantity = int(quantity)

