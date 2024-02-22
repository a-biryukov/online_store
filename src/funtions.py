from src.classes import Category, Product
import json
import os


def get_class_objects() -> list:
    """
    Загружает из файла список с данными, создаёт объекты классов Category и Products.
    Помещает список с объектами класса Product в атрибут products класса Category.
    :return: Список с объектами класса Category
    """
    current_file_path = os.path.abspath(__file__)
    parent_dir_path = os.path.dirname(os.path.dirname(current_file_path))
    file_path = os.path.join(parent_dir_path, "data", "products.json")

    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)

        category_objects = []

        for item in data:
            products_objects = []
            products = item.get("products")
            for i in products:
                product = Product(i.get("name"), i.get("description"), i.get("price"), i.get("quantity"))
                products_objects.append(product)

            category = Category(item.get("name"), item.get("description"), products_objects)
            category_objects.append(category)

    return category_objects
