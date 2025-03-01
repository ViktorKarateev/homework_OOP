from models import Product, Category
from utils import load_categories_from_json


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)


# Загружаем данные из products.json
categories = load_categories_from_json("products.json")

# Выводим загруженные категории
for category in categories:
    print(f"\nКатегория: {category.name}")
    print(f"Описание: {category.description}")
    print(f"Количество товаров: {len(category.products)}")
    print(f"Товары:\n{category.products}")
