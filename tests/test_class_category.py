import pytest

from src.class_category import Category


def test_init(category_smartphones, product_samsung, product_iphone):
    """ Тест на инициализацию объекта класса Category """
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Многофункциональное устройство"
    assert category_smartphones.products == [product_samsung, product_iphone]


def test_number(category_smartphones):
    """ Тест на подсчет объектов классов Category и Product """
    assert Category.number_of_categories == 1
    assert Category.number_of_products == 2


def test_str(category_smartphones, print_category):
    """ Тест метода str класса Category """
    assert str(category_smartphones) == print_category


def test_len(category_smartphones):
    """ Тест метода str класса Category """
    assert len(category_smartphones) == 13


def test_products(category_smartphones, product_iphone, product_samsung):
    """ Тест на получение списка продуктов """
    assert category_smartphones.products == [product_samsung, product_iphone]


def test_get_average_price(category_smartphones):
    """ Тест подсчета средней цены на товар в категории """
    assert category_smartphones.get_average_price() == 198461.54


def test_add_product(product_samsung, category_smartphones):
    """ Тест на добавление объекта класса Product в список товаров объекта класса Category """
    assert Category.number_of_products == 2
    assert len(category_smartphones) == 13
    category_smartphones.add_product(product_samsung)
    assert Category.number_of_products == 3
    assert len(category_smartphones) == 18
    with pytest.raises(TypeError):
        assert category_smartphones.add_product(category_smartphones)
