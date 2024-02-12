import pytest
from src.classes import Category, Product


@pytest.fixture()
def category_smartphone():
    return Category("Смартфоны", "Многофунциональное устройство", ["Samsung", "IPhone", "Xiaomi"])


@pytest.fixture()
def product_iphone():
    return Product("IPone", "512GB, Gray space", 210000.0, 8)


def test_init_category(category_smartphone):
    assert category_smartphone.name == "Смартфоны"
    assert category_smartphone.description == "Многофунциональное устройство"
    assert category_smartphone.products == ["Samsung", "IPhone", "Xiaomi"]


def test_init_product(product_iphone):
    assert product_iphone.name == "IPone"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8
