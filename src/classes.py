class Category:
    """Класс для представления категорий товаров"""

    name: str
    description: str
    products: list

    number_of_categories = 0
    number_of_products = 0

    def __init__(self, name: str, description: str, products: list) -> None:
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

    def __str__(self) -> str:
        """
        :return Информация о категории и товарах в формате:
                Название категории, количество товаров: X шт.
                    Продукт, X руб. Остаток: Y шт.
        """
        products_str = ""

        for i in self.__products:
            products_str += f"\n    {i.name}, {i.price} руб. Остаток: {i.quantity} шт."

        return f"""{self.name}, количество товаров: {self.__len__()} шт.{products_str}"""

    def __len__(self) -> int:
        """
        :return: Количество товаров в категории
        """

        return sum([product.quantity for product in self.__products])

    def add_product(self, product) -> None:
        """
        Добавляет объект товара в список
        :param product: Объескт класса Product
        :return: None
        """
        self.__products.append(product)
        Category.number_of_products += 1

    @property
    def products(self) -> list:
        """
        :return Список с объектами класса продукт
        """
        return self.__products


class Product:
    """Класс для представления товаров"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
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

    def __str__(self) -> str:
        """
        Возвращает строку в формате: Название продукта, X руб. Остаток: Y шт.
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.__len__()} шт."

    def __len__(self) -> int:
        """
        :return: Количество данного товара на складе
        """
        return self.quantity

    def __add__(self, other) -> float:
        """
        Складывает цены двух товаров и умножает на количество этих товаров на складе
        :param other: Объект класса Product
        :return: Сумма сложенных товаров с учетом их количества на складе
        """
        return self.price * self.quantity + other.price * other.quantity

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
    def price(self) -> None:
        """Ставит цену товара None"""
        self.__price = None

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, category):
        """
        Проверяет наличие продукта в списке продуктов,
            если он там есть,то добавляет количество и устанавливает максимальную цену,
            если нет, то создает объект класса Product
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество товара
        :param category: Объект класса Category
        :return: Объект класса Product или обновляет количество товара и цену в списке
        """
        products = category.products

        for product in products:
            if product.name == name:
                product.price = max(product.price, price)
                product.quantity += quantity
                print("\nЭтот товар уже есть на складе, количество в списке увеличено, цена выбрана наибольшая")
                return

        return cls(name, description, price, quantity)


class IterProducts:
    """Класс для итерации по списку товаров объекта класса Category"""

    def __init__(self, category):
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param category: Объект класса Category
        """
        self.category = category

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value < len(self.category.products) - 1:
            self.current_value += 1
            return self.category.products[self.current_value]
        else:
            raise StopIteration
