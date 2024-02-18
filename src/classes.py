class Category:
    """Класс для представления категорий товаров"""

    # Переменная для подсчета количества категорий товаров
    number_of_categories = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Название категории товаров
        :param description: Описание категории товаров
        :param products: Список товаров
        """
        self.name = name
        self.description = description
        self.products = products

        Category.number_of_categories += 1


class Product:
    """Класс для представления товаров"""

    # Переменная для подсчета количества уникальных товаров
    number_of_products = 0

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество данного товара на складе
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.number_of_products += 1
