import pytest

from src.classes_products import Product


def test_init(product_samsung):
    """Тест на инициализацию объекта класса Product"""
    assert product_samsung.name == "Samsung Galaxy C23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_str(category_smartphones, product_samsung, print_category):
    """Тест метода str класса Product"""
    assert str(product_samsung) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_len(product_samsung):
    """Тест метода len класса Product"""
    assert len(product_samsung) == 5


def test_add(product_samsung, product_iphone, category_smartphones):
    """Тест метода add класса Product"""
    assert product_iphone + product_samsung == 2580000.0
    with pytest.raises(TypeError):
        assert product_samsung + category_smartphones


def test_price(product_samsung):
    """Тест геттера, сеттера и делитера класса Product"""
    assert product_samsung.price == 180000.0
    product_samsung.price = 200000.0
    assert product_samsung.price == 200000.0
    product_samsung.price = 0
    assert product_samsung.price == 200000.0
    del product_samsung.price
    assert product_samsung.price is None


def test_add_product(category_smartphones, product_samsung):
    """ Тест метода add_product класса Product """
    assert category_smartphones.products[1].price == 210000.0
    assert category_smartphones.products[1].quantity == 8
    Product.add_product("Iphone 15", "512GB, Gray space", 300000.0,
                        2, category_smartphones)
    assert category_smartphones.products[1].price == 300000.0
    assert category_smartphones.products[1].quantity == 10
    assert type(Product.add_product("TV", "TV", 100, 5,
                                    category_smartphones)) == type(product_samsung)
