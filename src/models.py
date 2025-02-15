class Product:
    """Класс продукта с характеристиками."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Делаем цену приватной
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict, products_list: list):
        """Создает новый продукт из словаря, проверяя дубликаты."""
        for product in products_list:
            if product.name == data["name"]:
                product.quantity += data["quantity"]
                product.price = max(product.price, data["price"])
                return product

        return cls(data["name"], data["description"], data["price"], data["quantity"])

    @property
    def price(self):
        """Геттер: возвращает цену продукта."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер: проверяет и устанавливает цену."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    """Класс категории, содержащий список продуктов."""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products  # Делаем products приватным
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Добавляет продукт в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает список товаров в формате строки."""
        return "\n".join(
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        )