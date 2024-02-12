from src.classes import Category, Product
import pytest


@pytest.fixture()
def category_smartphone():
    return Category("Смартфоны", "Многофунциональное устройство", ["Samsung", "IPhone", "Xiaomi"])


@pytest.fixture()
def product_iphone():
    return Product("IPone", "512GB, Gray space", 210000.0, 8)