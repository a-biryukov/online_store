from abc import ABC, abstractmethod


class Goods(ABC):
    """ Абстрактный класс для наследования классами представляющих товары """

    @abstractmethod
    def __str__(self):
        """ Метод для получения информации информации о названии, цене и количестве товара """
        pass

    @abstractmethod
    def __len__(self):
        """ Метод получения количества товара на складе """
        pass

    @abstractmethod
    def __add__(self, other):
        """ Метод сложения объектов товаров """
        pass

    @abstractmethod
    def price(self):
        """ Геттер, сеттер и делитер для цены товара """
        pass

    @classmethod
    @abstractmethod
    def create_product(cls, *args):
        """ Метод создания объекта товара или обновления количества и цены, если товар уже есть на складе """
        pass


class MixinLog:
    """
     Миксин, который выводит в консоль информацию при создании объекта в формате:
        Название класса(свойства класса)
    """
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self) -> str:
        """
        :return: Строка с названием класса и свойствах
        """
        values_lst = list(self.__dict__.values())

        values_lst_ = []
        for i in values_lst:
            if type(i) is str:
                value = f"'{i}'"
                values_lst_.append(value)
            else:
                value = str(i)
                values_lst_.append(value)

        value_str = ", ".join(values_lst_)

        return f"{self.__class__.__name__}({value_str})"


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
            raise TypeError

        self.__products.append(product)
        Category.number_of_products += 1

    @property
    def products(self) -> list:
        """
        :return Список с объектами класса продукт
        """
        return self.__products


class Product(Goods, MixinLog):
    """ Класс для представления товаров """

    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, color=None) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количество данного товара на складе
        :param color: Цвет товара
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает строку в формате: Название продукта, X руб. Остаток: Y шт.
        """
        return f"{self.name}, {self.__price} руб. Остаток: {len(self)} шт."

    def __len__(self) -> int:
        """
        :return: Количество данного товара на складе
        """
        return self.quantity

    def __add__(self, other) -> float:
        """
        Складывает объекты одного класса
        :param other: Объект класса
        :return: Сумма сложенных цен товаров с учетом их количества на складе
        """
        if type(self) is not type(other):
            raise TypeError

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
        """ Ставит цену товара None """
        self.__price = None

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, category):
        """
        Проверяет наличие товара в списке товаров,
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
    """ Класс для итерации по списку товаров объекта класса Category """

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


class Smartphone(Product):
    """ Класс для представления смартфонов """

    name: str
    description: str
    price: float
    quantity: int
    color: str
    performance: float
    model: str
    memory: int

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str,
                 performance: float, model: str, memory: int) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количествотовара на складе
        :param performance: Производительность
        :param model: Модель
        :param memory: Объем встроенной памяти
        :param color: Цвет
        :param performance: производительность
        :param model: модель
        :param memory: Объем встроенной памяти
        """
        self.performance = performance
        self.model = model
        self.memory = memory
        super().__init__(name, description, price, quantity, color)

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, color: str,
                       performance: float, model: str, memory: int, category):
        """
        Проверяет наличие товара в списке товаров,
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

        return cls(name, description, price, quantity, color, performance, model, memory)


class LawnGrass(Product):
    """ Класс для представления газонной травы """

    name: str
    description: str
    price: float
    quantity: int
    country: str
    germination: int
    color: str

    def __init__(self, name: str, description: str, price: float, quantity: int, color: str,
                 country: str, germination: int) -> None:
        """
        Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.
        :param name: Название товара
        :param description: Описание товара
        :param price: Цена товара
        :param quantity: Количествотовара на складе
        :param country: Страна производитель
        :param germination: Срок прорастания
        :param color: Цвет
        :param country: Страна производитель
        :param germination: Срок произрастания
        """
        self.country = country
        self.germination = germination
        super().__init__(name, description, price, quantity, color)

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int, color: str,
                       country: str, germination: int, category):
        """
        Проверяет наличие товара в списке товаров,
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

        return cls(name, description, price, quantity, color, country, germination)
