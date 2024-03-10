from src.classes import MixinLog
from src.classes_products import Product


class Category(MixinLog):
    """ Класс для представления категорий товаров """

    name: str
    description: str
    products: list

    number_of_categories = 0
    number_of_products = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра класса.
        :param name: Название категории товаров
        :param description: Описание категории товаров
        :param products: Список товаров
        """
        self.name = name
        self.description = description
        self.__products = products
        super().__init__()

        Category.number_of_categories += 1
        Category.number_of_products += len(self.__products)

    def __str__(self) -> str:
        """
        :return Информация о категории и товарах в формате:
                Название категории, количество товаров: X шт.
                    Продукт, X руб. Остаток: Y шт.
        """
        return f"""{self.name}, количество товаров: {len(self)} шт."""

    def __len__(self) -> int:
        """
        :return: Количество товаров в категории
        """
        return sum([product.quantity for product in self.__products])

    def add_product(self, product) -> None:
        """
        Добавляет объект товара в список
        :param product: Объескт класса Product или его наследников
        :return: None
        """
        if not isinstance(product, Product):
            raise TypeError("Объект не является товаром")
        elif product.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.__products.append(product)
        Category.number_of_products += 1

    @property
    def products(self) -> list:
        """
        :return Список с объектами класса продукт
        """
        return self.__products

    def get_average_price(self):
        """
        Считает среднюю цену всех товаров в списке продуктов, если список продуктов пустой - возвращает 0
        :return: Средняя цена на товар в категории
        """
        total_price = sum([product.price * product.quantity for product in self.__products])
        total_products = len(self)

        try:
            average_price = total_price / total_products
        except ZeroDivisionError:
            return 0
        else:
            return round(average_price, 2)
