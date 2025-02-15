import os
from models import Product, Category
from utils import load_categories_from_json


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)  # Проверка работы геттера

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)  # Проверка добавления продукта
    print(category1.product_count)  # Проверка обновления счетчика продуктов

    products_list = [product1, product2, product3, product4]  # Создаем список товаров

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5},
        products_list  # Передаем список товаров
    )

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800  # Проверка сеттера (новая цена)
    print(new_product.price)

    new_product.price = -100  # Проверка защиты от отрицательной цены
    print(new_product.price)

    new_product.price = 0  # Проверка защиты от нуля
    print(new_product.price)


# Автоматически находим путь к JSON-файлу
file_path = os.path.join(os.path.dirname(__file__), "../data/products.json")

# Загружаем данные
categories = load_categories_from_json(file_path)


# Выводим загруженные категории
for category in categories:
    print(f"\nКатегория: {category.name}")
    print(f"Описание: {category.description}")
    print(f"Количество товаров: {len(category.products)}")
    print(f"Товары: {category.products}")
