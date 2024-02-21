from src.funtions import get_class_objects


def test_get_class_objects():
    assert type(get_class_objects()) == list
