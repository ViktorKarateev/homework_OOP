class Product:
    """Класс продукта с основными характеристиками."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (
            f"Product(name={self.name}, price={self.price}, "
            f"quantity={self.quantity})"
        )


class Category:
    """Класс категории, содержащий список продуктов."""

    category_count = 0  # Количество категорий
    product_count = 0  # Количество всех товаров

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчики
        Category.category_count += 1
        Category.product_count += len(products)

    def __repr__(self):
        return f"Category(name={self.name}, products={len(self.products)})"
