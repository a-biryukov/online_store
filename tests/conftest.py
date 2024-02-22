import pytest
from src.classes import Category, Product


PROD = [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      }
      ]

CAT = {
    "name": "Смартфоны",
    "description": "Многофункциональное устройство",
    "products": [
        Product(PROD[0].get("name"), PROD[0].get("description"), PROD[0].get("price"), PROD[0].get("quantity")),
        Product(PROD[1].get("name"), PROD[1].get("description"), PROD[1].get("price"), PROD[1].get("quantity"))
    ]
}

PRINT_CAT = """Смартфоны, количество товаров: 13 шт.
    Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.
    Iphone 15, 210000.0 руб. Остаток: 8 шт."""


@pytest.fixture
def category_smartphones():
    Category.number_of_categories = 0
    Category.number_of_products = 0
    return Category(CAT.get("name"), CAT.get("description"), CAT.get("products"))


@pytest.fixture
def product_samsung():
    Category.number_of_products = 0
    return CAT.get("products")[0]


@pytest.fixture
def product_iphone():
    Category.number_of_products = 0
    return CAT.get("products")[1]


@pytest.fixture
def print_category():
    return PRINT_CAT
