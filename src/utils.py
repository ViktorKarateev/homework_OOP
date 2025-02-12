import json
from models import Product, Category


def load_categories_from_json(file_path: str) -> list:
    """Загружает категории и товары из JSON-файла и создает объекты."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = [
            Product(
                p["name"], p["description"], p["price"], p["quantity"]
            )
            for p in category_data["products"]
        ]
        category = Category(
            category_data["name"], category_data["description"], products
        )
        categories.append(category)

    return categories
