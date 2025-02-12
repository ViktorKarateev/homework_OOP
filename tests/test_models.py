import pytest
from src.models import Product, Category


def test_product_initialization():
    """Тест корректного создания продукта."""
    product = Product("Test Product", "Test Description", 99.99, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 99.99
    assert product.quantity == 10


def test_category_initialization():
    """Тест корректного создания категории."""
    product1 = Product("Product 1", "Desc 1", 50.0, 5)
    product2 = Product("Product 2", "Desc 2", 100.0, 10)
    category = Category("Test Category", "Category Description", [product1, product2])

    assert category.name == "Test Category"
    assert category.description == "Category Description"
    assert len(category.products) == 2


def test_category_counters():
    """Тест подсчета количества категорий и товаров."""
    # Сбрасываем счётчики перед тестами
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Product 1", "Desc 1", 50.0, 5)
    product2 = Product("Product 2", "Desc 2", 100.0, 10)
    category1 = Category("Category 1", "Desc 1", [product1, product2])
    category2 = Category("Category 2", "Desc 2", [])

    assert Category.category_count == 2
    assert Category.product_count == 2  # Только два продукта добавили

