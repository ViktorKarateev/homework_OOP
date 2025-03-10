# Homework OOP

##  Описание  
Проект по изучению объектно-ориентированного программирования (OOP) на Python.  
Реализованы классы `Product`, `Category`, их наследники, ограничения сложения товаров и работы с категориями.  

##  Функциональность проекта  

### **1. Класс `Product`**  
Класс `Product` отвечает за представление товаров и включает в себя:  
- **Название товара (`name`)**  
- **Описание (`description`)**  
- **Цена (`price`)**  
- **Количество на складе (`quantity`)**  

**Дополнительно добавлено:**  
- **Приватный атрибут `__price`** (защищает цену от прямого изменения).  
- **Геттер `@property price`** → возвращает цену товара.  
- **Сеттер `@price.setter`** → защищает цену от нулевых и отрицательных значений.  
- **Метод `new_product()`** → создаёт новый продукт из словаря, проверяет дубликаты.  
- **Магический метод `__add__`** → теперь товары можно складывать только **одного типа**, иначе выбрасывается `TypeError`.  

### **2. Классы-наследники**  
Реализованы **два новых класса товаров**:  
- `Smartphone` (наследник `Product`), который содержит:  
  - `efficiency` (производительность)  
  - `model` (модель)  
  - `memory` (объём встроенной памяти)  
  - `color` (цвет)  
- `LawnGrass` (наследник `Product`), который содержит:  
  - `country` (страна-производитель)  
  - `germination_period` (срок прорастания)  
  - `color` (цвет)  
**Теперь метод `__add__` работает только для товаров одного типа!**  

### **3. Класс `Category`**  
Класс `Category` отвечает за категории товаров и включает:  
- **Название категории (`name`)**  
- **Описание (`description`)**  
- **Список товаров (`products`)**  

**Дополнительно добавлено:**  
- **Приватный атрибут `__products`** (список товаров защищён от изменения извне).  
- **Метод `add_product()`**:  
  - Добавляет только `Product` и его наследников.  
  - Попытка добавить **любой другой объект** вызовет `TypeError`.  
- **Геттер `@property products`**:  
  - Теперь товары в категории отображаются с учётом их строкового представления `__str__`.  

### **4. Загрузка товаров из JSON**  
Добавлена функция `load_categories_from_json(file_path: str)`, которая загружает данные из `products.json` и создаёт объекты классов.  
**Путь к файлу теперь обрабатывается автоматически, чтобы избежать ошибок при запуске.**  

### **5. Оптимизация строкового представления товаров**  
- Реализован метод `__str__` для `Product` → теперь товары автоматически форматируются в строку.  
- Реализован метод `__str__` для `Category` → отображает название категории и количество товаров.  

### **6. Итерация по товарам в категории (доп. задание)**  
Реализован класс-итератор, позволяющий **перебирать товары** в категории с помощью `for`.  

### 7. Абстрактный класс `BaseProduct`
- Родительский класс для всех товаров.
- Определяет **базовые атрибуты** (`name`, `description`, `price`, `quantity`).
- Содержит **абстрактный метод `get_info()`**, который должен реализовать каждый продукт.

### 8. Миксин `LoggingMixin`
- Выводит в консоль **информацию о созданном объекте** (его класс и параметры).
- Используется в классе `Product` и его наследниках.

##  Запуск проекта
```bash
poetry install  # Установка зависимостей
poetry run python src/main.py  # Запуск программы
poetry run pytest  # Запуск тестов

