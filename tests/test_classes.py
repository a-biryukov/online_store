import pytest
from src.classes import Category


@pytest.fixture()
def category_smartphone():
    return Category("Смартфоны", "Многофунциональное устройство", ["Samsung", "IPhane", "Xiaomi"])


def test_init(category_smartphone):
    assert category_smartphone.name == "Смартфоны"
    assert category_smartphone.description == "Многофунциональное устройство"
    assert category_smartphone.goods == ["Samsung", "IPhane", "Xiaomi"]