import pytest

from src import category
from src.category import Category
from src.product import Product


@pytest.fixture
def product_one_instance():
    prod_one_data = {
    'name': 'Vivo 53s',
    'description': '256GB, Синий цвет, 150mp',
    'price': 21000.0,
    'count': 20
}
    product_one_instance = Product.create_product(prod_one_data)
    return product_one_instance

def test_create_product(product_one_instance):
    assert product_one_instance.name == 'Vivo 53s'
    assert product_one_instance.description == '256GB, Синий цвет, 150mp'
    assert product_one_instance.price == 21000.0
    assert product_one_instance.count == 20

def test_str():
    product_one_instance = Product('Vivo 53s', '256GB, Синий цвет, 150mp', 21000.0, 20)
    assert str(product_one_instance) == 'Vivo 53s, 21000.0 руб. Остаток: 20 шт'

def test_add():
    product_one_instance = Product('Vivo 53s', '256GB, Синий цвет, 150mp', 21000.0, 20)
    product_two_instance = Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200mp', 100000.0, 10)
    assert product_one_instance + product_two_instance == '1420000.0 руб. общая цена всех продуктов на складе.\nОбщее количество продуктов 30 шт на склад'

def test_price():
    product_one_instance = Product('Vivo 53s', '256GB, Синий цвет, 150mp', 21000.0, 20)
    assert product_one_instance.price == 21000.0

def test_prices():
    """Доработать изменение цены """
    pass

def test_add_product():
    category = Category('Смартфоны', 'Категория для смартфонов', [])
    product_one_instance = Product('Vivo 53s', '256GB, Синий цвет, 150mp', 21000.0, 20)
    product_two_instance = Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200mp', 100000.0, 10)
    category.add_products(product_one_instance)
    category.add_products(product_two_instance)
    assert category.total_categories == 2
    assert category.total_products == 0

# def test_category():
#     category = Category('Смартфоны', 'Категория для смартфонов', [])
#     product_one_instance = Product('Vivo 53s', '256GB, Синий цвет, 150mp', 21000.0, 20)
#     category.add_products(product_one_instance)
#     assert category == 'Смартфоны, количество продуктов 20 шт'


@pytest.fixture(autouse=True)
def reinit_cat_attributes():
    Category.total_categories = 0
    Category.total_products = 0


