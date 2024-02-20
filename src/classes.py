class Category:
    """Класс для представления категорий товаров"""

    name: str
    description: str
    products: list

    number_of_categories = 0
    number_of_products = 0

    def __init__(self, name, description, products) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Название категории товаров
        :param description: Описание категории товаров
        :param products: Список товаров
        """
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_categories += 1
        Category.number_of_products += len(self.__products)

    def add_product(self, product) -> None:
        """
        Добавляет объект товара в список
        :param product: Объескт класса Product
        :return: None
        """
        name = product.name
        description = product.description
        price = product.price
        quantity = product.quantity

        product = {
            "name": name,
            "description": description,
            "price": price,
            "quantity": quantity
        }

        self.__products.append(product)
        Category.number_of_products += 1

    @property
    def products(self) -> None:
        """
        Выводит список товаров в формате: Продукт, X руб. Остаток: Y шт.
        """
        for i in self.__products:
            print(f"{i.get("name")}, {i.get("price")} руб. Остаток: {i.get("quantity")} шт.")


class Product:
    """Класс для представления товаров"""

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
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для получения цены товара"""
        return self.__price

    @price.setter
    def price(self, new_price) -> None:
        """
        Меняет цену товара
        Если новая цена ниже или равна нулю выводит сообщение "Введена некоректная цена"
        Если новая цена ниже предыдущей запрашивает подтверждение через ввод (y/n)
        :param new_price: Новая цена на товар
        :return: None
        """
        new_price = float(new_price)
        if new_price <= 0:
            print("Введена некорректная цена")
        elif 0 < new_price < self.__price:
            print("Введенная цена ниже предыдущей.")
            user_enter = input("Установить новую цену? (y/n): ").lower()
            if user_enter == "y":
                self.__price = new_price
        else:
            self.__price = new_price

    @price.deleter
    def price(self):
        """Ставит цену товара None"""
        self.__price = None

    @classmethod
    def create_product(cls):
        """
        Создает объект класса Product
        """
        name = input("Введите название товара: ")
        description = input("Введите описание товара: ")
        price = float(input("Введите цену товара: "))
        quantity = float(input("Введите количество товара: "))

        return cls(name, description, price, quantity)
