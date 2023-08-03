import json
import yaml


def open_file(file_path: str):
    """
    Open and load a file in YAML or JSON format.

    This function takes a file path as input, opens the file, and then
    attempts to load its contents as YAML or JSON data, depending on the file
    extension. The loaded data is returned.

    :param file_path: The path to the file to be opened and loaded.
    :type file_path: str
    :return: The loaded data from the file.
    :rtype: dict or list
    """

    with open(file_path, "r") as file:
        return load_file(file_path, file)


def load_file(path: str, file) -> dict:
    """
    Load data from a file.

    This function takes a file path and an open file object as input. It
    detects the file format based on the file path's extension (.json for JSON
    or .yaml or .yml for YAML) and loads the data from the file accordingly.
    The loaded data is returned.

    :param path: The path to the file.
    :type path: str
    :param file: An open file object.
    :type file: file
    :return: The loaded data from the file.
    :rtype: dict
    """
    if path.endswith(".yaml") or path.endswith(".yml"):
        return yaml.safe_load(file)
    elif path.endswith(".json"):
        return json.load(file)
