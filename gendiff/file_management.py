import json
import yaml


def open_file(file_path):
    with open(file_path, "r") as file:
        return load_file(file_path, file)


def load_file(path, file):
    if path.endswith(".yaml") or path.endswith(".yml"):
        return yaml.safe_load(file)
    elif path.endswith(".json"):
        return json.load(file)
