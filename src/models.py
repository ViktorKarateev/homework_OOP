class Product:
    """Класс продукта с характеристиками."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Делаем цену приватной
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер: проверяет и устанавливает цену."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает стоимость товаров на складе, если товары одного типа."""
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного класса")

        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, data: dict, products_list: list):
        """Создает новый продукт из словаря, проверяя дубликаты."""
        for product in products_list:
            if product.name == data["name"]:
                product.quantity += data["quantity"]
                product.price = max(product.price, data["price"])
                return product

        return cls(data["name"], data["description"], data["price"], data["quantity"])


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
        """Добавляет продукт в категорию, если он является экземпляром Product или его наследников."""
        if not isinstance(product, Product):  # Проверяем, является ли продукт экземпляром Product или его наследников
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает список товаров в формате строки (использует __str__)."""
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class Smartphone(Product):
    """Класс для смартфонов, наследуется от Product."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # Производительность
        self.model = model  # Модель
        self.memory = memory  # Встроенная память
        self.color = color  # Цвет


class LawnGrass(Product):
    """Класс для газонной травы, наследуется от Product."""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country  # Страна-производитель
        self.germination_period = germination_period  # Срок прорастания
        self.color = color  # Цвет
