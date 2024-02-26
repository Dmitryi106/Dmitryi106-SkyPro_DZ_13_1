from category import Category
from src import product

from src.product import Product


def main():
    prod_one_data = {
        'name': 'Samsung Galaxy C23 Ultra',
        'description': '256GB, Серый цвет, 200mp',
        'price': 100000.0,
        'count': 10
    }
    prod_two_data = {
        'name': 'Iphone 15',
        'description': '256GB, Black space',
        'price': 200000.0,
        'count': 5
    }

    product_one_instance = Product.create_product(prod_one_data)
    product_two_instance = Product.create_product(prod_two_data)
    print(type(product_one_instance))
    print(product_one_instance)
    all_products = [product_two_instance, product_one_instance]
    category = Category('Смартфоны', 'Категория для смартфонов', all_products)
    print(category)
    print(Product.price)
    print(product_one_instance + product_two_instance)
    print(category.products)
    print(Product.create_product(prod_two_data))
    print(category.total_categories)
    print(category.total_products)


if __name__ == '__main__':
    main()
