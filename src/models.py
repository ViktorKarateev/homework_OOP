from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех товаров."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Защищаемый атрибут
        self.quantity = quantity

    @abstractmethod
    def get_info(self):
        """Абстрактный метод, который должен реализовать каждый продукт."""
        pass

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Ошибка: Цена не может быть отрицательной или равной нулю")


class LoggingMixin:
    """Миксин для логирования создания объектов."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект: {self.__class__.__name__} с параметрами {self.__dict__}")


class Product(LoggingMixin, BaseProduct):
    """Класс продукта с характеристиками."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)  # Вызываем конструктор родителя

    def get_info(self):
        """Метод, который должен быть реализован в каждом классе-наследнике BaseProduct."""
        return f"{self.name} ({self.description}) - {self.price} руб."

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
    """Класс смартфона — наследник `Product`."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def get_info(self):
        return f"{self.name} ({self.model}) - {self.memory}GB, {self.color}"


class LawnGrass(Product):
    """Класс газонной травы — наследник `Product`."""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def get_info(self):
        return f"{self.name} (Производство: {self.country}) - {self.color}, {self.germination_period}"
