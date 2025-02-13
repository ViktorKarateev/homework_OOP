import pytest  # noqa: F401
from src.models import Product, Category


def test_product_initialization():
    """Проверка, что объект Product создается корректно."""
    product = Product("Laptop", "Gaming laptop", 1500.0, 3)
    assert product.name == "Laptop"
    assert product.description == "Gaming laptop"
    assert product.price == 1500.0
    assert product.quantity == 3


def test_category_initialization():
    """Проверка, что объект Category создается корректно."""
    product1 = Product("Mouse", "Wireless Mouse", 50.0, 10)
    product2 = Product("Keyboard", "Mechanical Keyboard", 120.0, 5)
    category = Category("Accessories", "PC Accessories", [product1, product2])

    assert category.name == "Accessories"
    assert category.description == "PC Accessories"
    assert len(category.products) == 2
    assert category.products[0].name == "Mouse"
    assert category.products[1].price == 120.0


def test_category_product_count():
    """Проверка, что Category корректно считает общее количество товаров."""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Headphones", "Bluetooth Headphones", 200.0, 7)
    product2 = Product("Monitor", "4K Monitor", 500.0, 3)

    category1 = Category("Audio", "Audio Devices", [product1])
    category2 = Category("Displays", "Monitor Displays", [product2])

    assert category1  # Теперь переменная используется
    assert category2  # Теперь переменная используется

    assert Category.product_count == 2  # Всего два продукта


def test_category_count():
    """Проверка, что Category корректно считает количество категорий."""
    Category.category_count = 0

    category1 = Category("Smartphones", "Mobile Devices", [])
    category2 = Category("Tablets", "Tablet Devices", [])
    category3 = Category("Wearables", "Smartwatches", [])

    assert category1  # Теперь переменная используется
    assert category2  # Теперь переменная используется
    assert category3  # Теперь переменная используется

    assert Category.category_count == 3  # Всего три категории
