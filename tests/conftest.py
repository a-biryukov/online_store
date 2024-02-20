import pytest
from src.classes import Category, Product


CATEGORY = {
    "name": "Смартфоны",
    "description": "Многофункциональное устройство",
    "products": [
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
    }


@pytest.fixture()
def category_smartphones():
    return Category(CATEGORY.get("name"), CATEGORY.get("description"), CATEGORY.get("products"))


@pytest.fixture()
def product_samsung():
    prod_1 = CATEGORY.get("products")[0]
    return Product(prod_1.get("name"), prod_1.get("description"), prod_1.get("price"), prod_1.get("quantity"))


@pytest.fixture()
def product_iphone():
    prod_2 = CATEGORY.get("products")[1]
    return Product(prod_2.get("name"), prod_2.get("description"), prod_2.get("price"), prod_2.get("quantity"))
