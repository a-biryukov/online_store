import json
import os


def get_():
    current_file_path = os.path.abspath(__file__)
    parent_dir_path = os.path.dirname(os.path.dirname(os.path.dirname(current_file_path)))
    file_path = os.path.join(parent_dir_path, "data", "products.json")

    with open(file_path) as file:
        products_lst = json.load(file)
