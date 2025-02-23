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

    # Новый способ проверки количества товаров:
    assert len(category.products.split("\n")) == 2  # Разбиваем строку на список товаров


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


def test_add_product():
    """Проверяем, что метод add_product() добавляет продукт в категорию."""
    category = Category("Тестовая категория", "Описание", [])
    product = Product("Тестовый товар", "Описание товара", 999.99, 10)

    category.add_product(product)

    assert len(category.products.split("\n")) == 1  # Проверяем, что продукт добавился
    assert "Тестовый товар" in category.products  # Проверяем, что имя товара есть в списке
    assert "999.99 руб." in category.products  # Проверяем, что цена товара корректно отображается


def test_new_product():
    """Проверяем, что метод new_product() создает товар из словаря."""
    products_list = []
    product_data = {"name": "iPad Pro", "description": "256GB, Silver", "price": 120000.0, "quantity": 3}

    new_product = Product.new_product(product_data, products_list)

    assert new_product.name == "iPad Pro"
    assert new_product.description == "256GB, Silver"
    assert new_product.price == 120000.0
    assert new_product.quantity == 3


def test_price_setter():
    """Проверяем защиту от установки отрицательной цены."""
    product = Product("MacBook Air", "13-inch, M1", 100000.0, 5)

    product.price = 50000  # Корректное изменение цены
    assert product.price == 50000  # Цена изменилась

    product.price = -1000  # Попытка установить отрицательную цену
    assert product.price == 50000  # Цена не изменилась


def test_product_str():
    """Проверяем строковое представление продукта."""
    product = Product("Test Product", "Test Description", 100.0, 5)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 5 шт."


def test_category_str():
    """Проверяем строковое представление категории."""
    product1 = Product("Mouse", "Wireless Mouse", 50.0, 10)
    product2 = Product("Keyboard", "Mechanical Keyboard", 120.0, 5)
    category = Category("Accessories", "PC Accessories", [product1, product2])

    assert str(category) == "Accessories, количество продуктов: 15 шт."


def test_product_add():
    """Проверяем сумму стоимости товаров через __add__."""
    product1 = Product("Mouse", "Wireless Mouse", 50.0, 10)  # 50 * 10 = 500
    product2 = Product("Keyboard", "Mechanical Keyboard", 120.0, 5)  # 120 * 5 = 600

    assert product1 + product2 == 1100  # 500 + 600 = 1100


def test_product_add_invalid():
    """Проверяем, что нельзя сложить продукт с не-продуктом."""
    product = Product("Mouse", "Wireless Mouse", 50.0, 10)

    with pytest.raises(TypeError):
        product + 100  # Ошибка, так как складываем с числом
