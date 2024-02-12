class Base:
    """Базовый класс для наследования"""
    def __init__(self, name: str, description: str) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Название
        :param description: Описание
        """
        self.name = name
        self.description = description


class Category(Base):
    """Класс для представления категорий товаров"""
    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Название категории товаров
        :param description: Описание категории товаров
        :param products: Список товаров
        """
        super().__init__(name, description)
        self.products = products


class Product(Base):
    """Класс для представления товаров"""
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество данного товара на складе
        """
        super().__init__(name, description)
        self.price = price
        self.quantity = quantity
