from src.classes import Category, Product
import json
import os


def get_class_objects(class_name: str) -> list:
    current_file_path = os.path.abspath(__file__)
    parent_dir_path = os.path.dirname(os.path.dirname(current_file_path))
    file_path = os.path.join(parent_dir_path, "data", "products.json")

    with open(file_path) as file:
        data = json.load(file)

        class_objects = []

        for item in data:
            if class_name == "Category":
                category = Category(item.get("name"), item.get("description"), item.get("products"))
                class_objects.append(category)
            elif class_name == "Product":
                products = item.get("products")
                for i in products:
                    product = Product(i.get("name"), i.get("description"), i.get("price"), i.get("quantity"))
                    class_objects.append(product)

    return class_objects
