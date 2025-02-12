class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"


class Category:
    category_count = 0  # Атрибут класса, считает категории
    product_count = 0    # Атрибут класса, считает товары

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчики
        Category.category_count += 1
        Category.product_count += len(products)

    def __repr__(self):
        return f"Category(name={self.name}, products={len(self.products)})"
