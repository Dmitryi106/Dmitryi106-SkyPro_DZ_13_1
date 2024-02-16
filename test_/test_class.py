import pytest

from src.category import Category
from src.product import Product

@pytest.fixture
def test_total_products():
    return Category("Видеокарты", "игровые видеокарты для компьютера",["MSI NVIDIA GeForce RTX 4060TI", "MSI NVIDIA GeForce RTX 4070Ti", "MSI NVIDIA Ge"])

def test_total_product(test_total_products):
    assert Category.total_products == 3


@pytest.fixture
def test_total_categories():
    return Category("Видеокарты", "игровые видеокарты для компьютера",["MSI NVIDIA GeForce RTX 4060TI", "MSI NVIDIA GeForce RTX 4070Ti", "MSI NVIDIA Ge"])

def test_total_category(test_total_categories):
    assert Category.total_categories == 1


@pytest.fixture
def test_Category():
    return Category("Видеокарты", "игровые видеокарты для компьютера", ["MSI NVIDIA GeForce RTX 4060TI", "видеопамять 8Gb, Тип видеопамяти GDDR6, Частота видеопамяти 18000 МГц", 59000, 10])

def test_init_category(test_Category):
    assert test_Category.name == "Видеокарты"
    assert test_Category.description == "игровые видеокарты для компьютера"
    assert test_Category.product == 'MSI NVIDIA GeForce RTX 4060TI, 59000 руб. Остаток: 10 шт'
    assert Category.total_categories == 1


@pytest.fixture
def test_Product():
    return Product("MSI NVIDIA GeForce RTX 4060TI", 'видеопамять 8Gb, Тип видеопамяти GDDR6, Частота видеопамяти 18000 МГц', 70000, 10)

def test_init_product(test_Product):
    assert test_Product.name == "MSI NVIDIA GeForce RTX 4060TI"
    assert test_Product.description == 'видеопамять 8Gb, Тип видеопамяти GDDR6, Частота видеопамяти 18000 МГц'
    assert test_Product.price == 70000.0
    assert test_Product.quantity == 10
def test_price(test_Product):
    test_Product.price = 90000
    assert test_Product.price == 90000.0
    test_Product.price = 0
    assert test_Product.price == 90000.0


@pytest.fixture(autouse=True)
def reinit_cat_attributes():
    Category.total_categories = 0
    Category.total_products = 0

