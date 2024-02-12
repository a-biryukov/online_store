from src.classes import Category, Product


def test_init_category(category_smartphone):
    assert category_smartphone.name == "Смартфоны"
    assert category_smartphone.description == "Многофунциональное устройство"
    assert category_smartphone.products == ["Samsung", "IPhone", "Xiaomi"]


def test_init_product(product_iphone):
    assert product_iphone.name == "IPone"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_number_of_categories(category_smartphone):
    assert Category.number_of_categories == 1


def test_number_of_products(product_iphone):
    assert Product.number_of_products == 1
