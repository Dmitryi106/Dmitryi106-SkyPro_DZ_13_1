import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def test_Category():
    return Category("Видеокарты", "игровые видеокарты для компьютера",["MSI NVIDIA GeForce RTX 4060TI", "MSI NVIDIA GeForce RTX 4070Ti, MSI NVIDIA Ge"])

def test_init_category(test_Category):
    assert test_Category.name == "Видеокарты"
    assert test_Category.description == "игровые видеокарты для компьютера"
    assert test_Category.products == ["MSI NVIDIA GeForce RTX 4060TI", "MSI NVIDIA GeForce RTX 4070Ti, MSI NVIDIA Ge"]
    assert Category.total_categories == 1

@pytest.fixture
def test_Product():
    return Product("MSI NVIDIA GeForce RTX 4060TI, MSI", 'игровая видеокарта', 70000, 10)
def test_init_product(test_Product):
    assert test_Product.name == "MSI NVIDIA GeForce RTX 4060TI, MSI"
    assert test_Product.description == 'игровая видеокарта'
    assert test_Product.price == 70000.0
    assert test_Product.quantity == 10

@pytest.fixture
def test_total_products():
    return Category("Видеокарты", "игровые видеокарты для компьютера",["MSI NVIDIA GeForce RTX 4060TI", "MSI NVIDIA GeForce RTX 4070Ti, MSI NVIDIA Ge"])

def test_total_product(test_total_products):
    assert Category.total_products == 4

@pytest.fixture
def test_total_categories():
    return Category("Видеокарты", "игровые видеокарты для компьютера",["MSI NVIDIA GeForce RTX 4060TI", "MSI NVIDIA GeForce RTX 4070Ti, MSI NVIDIA Ge"])

def test_total_category(test_total_categories):
    assert Category.total_categories == 1