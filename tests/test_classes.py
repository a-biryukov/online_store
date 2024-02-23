from src.classes import Category, Product, IterProducts


def test_init_category(category_smartphones, product_samsung, product_iphone):
    """Тест на инициализацию объекта класса Category"""
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Многофункциональное устройство"
    assert category_smartphones.products == [product_samsung, product_iphone]


def test_number(category_smartphones):
    """Тест на подсчет объектов классов Category и Product"""
    assert Category.number_of_categories == 1
    assert Category.number_of_products == 2


def test_init_product(product_samsung):
    """Тест на инициализацию объекта класса Product"""
    assert product_samsung.name == "Samsung Galaxy C23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_str(category_smartphones, product_samsung, print_category):
    """Тест метода str классов Category и Product"""
    assert str(category_smartphones) == print_category
    assert str(product_samsung) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_len(category_smartphones, product_samsung):
    """Тест метода str классов Category и Product"""
    assert len(category_smartphones) == 13
    assert len(product_samsung) == 5


def test_products(category_smartphones, product_iphone, product_samsung):
    """Тест на получение списка продуктов"""
    assert category_smartphones.products == [product_samsung, product_iphone]


def test_add(product_samsung, product_iphone):
    """Тест метода add класса Product"""
    assert product_iphone + product_samsung == 2580000.0


def test_price(product_samsung):
    """Тест геттера, сеттера и делитера класса Product"""
    assert product_samsung.price == 180000.0
    product_samsung.price = 200000.0
    assert product_samsung.price == 200000.0
    product_samsung.price = 0
    assert product_samsung.price == 200000.0
    del product_samsung.price
    assert product_samsung.price is None


def test_iter_category(category_smartphones):
    """Тест класса IterProducts"""
    assert [product.name for product in IterProducts(category_smartphones)] == ["Samsung Galaxy C23 Ultra", "Iphone 15"]


def test_add_product(product_samsung, category_smartphones):
    """Тест на добавление объекта класса Product в список товаров объекта класса Category"""
    assert Category.number_of_products == 2
    assert len(category_smartphones) == 13
    category_smartphones.add_product(product_samsung)
    assert Category.number_of_products == 3
    assert len(category_smartphones) == 18


def test_create_product(category_smartphones):
    """
    Тест на обновление цены и количества товара при его создании,
    если этот товар уже есть в списке объектов класса Product
    """
    assert category_smartphones.products[1].price == 210000.0
    assert category_smartphones.products[1].quantity == 8
    Product.create_product("Iphone 15", "512GB, Gray space", 300000.0, 2, category_smartphones)
    assert category_smartphones.products[1].price == 300000.0
    assert category_smartphones.products[1].quantity == 10
