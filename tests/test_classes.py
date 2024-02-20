from src.classes import Category


def test_init_category(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Многофункциональное устройство"


def test_number_of_categories(category_smartphones):
    assert Category.number_of_categories == 1


def test_number_of_products(category_smartphones):
    assert Category.number_of_products == 1


def test_add_product(product_samsung, category_smartphones):
    assert Category.number_of_products == 1
    category_smartphones.add_product(product_samsung)
    assert Category.number_of_products == 2


def test_init_product(product_samsung):
    assert product_samsung.name == "Samsung Galaxy C23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_price(product_samsung):
    assert product_samsung.price == 180000.0
    product_samsung.price = 200000.0
    assert product_samsung.price == 200000.0
    product_samsung.price = 0
    assert product_samsung.price == 200000.0
    del product_samsung.price
    assert product_samsung.price is None


