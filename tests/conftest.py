import pytest
from src.classes import Category, Product


CATEGORY = {
    "name": "Смартфоны",
    "description": "Многофункциональное устройство",
    "products": [{
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      }]
    }


@pytest.fixture()
def category_smartphones():
    return Category(CATEGORY.get("name"), CATEGORY.get("description"), CATEGORY.get("products"))


@pytest.fixture()
def product_samsung():
    prod_1 = CATEGORY.get("products")[0]
    return Product(prod_1.get("name"), prod_1.get("description"), prod_1.get("price"), prod_1.get("quantity"))


@pytest.fixture()
def product():
    return CATEGORY.get("products")[0]
