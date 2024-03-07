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
