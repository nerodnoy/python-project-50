import itertools
from gendiff.formatters.converters import convert_to_str
from gendiff.constants import (
    TEMPLATE_NESTED,
    TEMPLATE_STYLISH
)


def create_stylish(diff: list) -> str:
    """
    Create the difference tree in "stylish" format.

    This function takes the difference tree as input and returns it formatted
    in the "stylish" format, visually representing the differences in a
    human-readable way with indentation and symbolic annotations.

    :param diff: Difference tree as a list of dictionaries.
    :type diff: list
    :return: String representation of the difference in "stylish" format.
    :rtype: str
    """

    result = format_diff(diff)
    return result


def format_diff(data: list, depth: int = 0) -> str:
    """
    Recursively format the difference tree into a "stylish" formatted string.

    This function iterates through the difference tree nodes and returns a
    string representation of the differences in the "stylish" format. It uses
    indentation to represent nested structures.

    :param data: Difference tree node or subtree as a list of dictionaries.
    :type data: list[dict]
    :param depth: Current depth level for indentation (optional).
    :type depth: int
    :return: String representation of the difference in "stylish" format.
    :rtype: str
    """

    lines = []
    indent = depth * "    "
    data.sort(key=lambda node: node["key"])

    for node in data:
        if node["type"] == "nested":
            lines.append(format_nested_node(node, indent, depth))
        else:
            lines.extend(format_single_node(node, indent, depth))

    result = itertools.chain("{", lines, [indent + "}"])
    return "\n".join(result)


def format_nested_node(node: dict, indent: str, depth: int) -> str:
    """
    Format a nested node in the "stylish" format.

    This function formats a nested node with its children recursively and
    returns a string representation for the node in "stylish" format.

    :param node: Nested node representing a difference.
    :type node: dict
    :param indent: Indentation string for the current depth level.
    :type indent: str
    :param depth: Current depth level.
    :type depth: int
    :return: String representation of the nested node in "stylish" format.
    :rtype: str
    """

    nested_lines = format_diff(node["children"], depth + 1)
    return TEMPLATE_NESTED.format(indent, node["key"], nested_lines)


def format_single_node(node: dict, indent: str, depth: int) -> list:
    """
    Format a single node in the "stylish" format.

    This function formats a single node representing a difference and returns
    a list of strings representing the difference lines for the node in
    "stylish" format.

    :param node: Single node representing a difference.
    :type node: dict
    :param indent: Indentation string for the current depth level.
    :type indent: str
    :param depth: Current depth level.
    :type depth: int
    :return: List of strings representing the difference lines for the node
             in "stylish" format.
    :rtype: list
    """

    lines = []
    if node["type"] == "removed":
        lines.append(format_line(
            node["key"], node.get("old_value"), "-", depth))
    elif node["type"] == "added":
        lines.append(format_line(
            node["key"], node.get("new_value"), "+", depth))
    elif node["type"] == "unchanged":
        lines.append(format_line(
            node["key"], node.get("old_value"), " ", depth))
    elif node["type"] == "updated":
        lines.append(format_line(
            node["key"], node.get("old_value"), "-", depth))
        lines.append(format_line(
            node["key"], node.get("new_value"), "+", depth))
    return lines


def format_line(key: str, value: any, sign: str, depth: int) -> str:
    """
    Format a line in the "stylish" format.

    This function formats a line representing a difference and returns a
    string representation for the line in "stylish" format.

    :param key: Key representing the difference.
    :type key: str
    :param value: Value associated with the key.
    :type value: any
    :param sign: Symbol representing the type of difference.
    :type sign: str
    :param depth: Current depth level.
    :type depth: int
    :return: String representation of the line in "stylish" format.
    :rtype: str
    """

    indent = "    " * depth
    lines = []

    if isinstance(value, dict):
        lines.append(TEMPLATE_STYLISH.format(
            indent, sign, key, format_dict(value, depth + 1)))
    else:
        lines.append(TEMPLATE_STYLISH.format(
            indent, sign, key, convert_to_str(value)))

    return "\n".join(lines)


def format_dict(dic: dict, depth: int) -> str:
    """
    Format a dictionary in the "stylish" format.

    This function formats a dictionary representing a nested structure and
    returns a string representation for the dictionary in "stylish" format.

    :param dic: Dictionary representing the nested structure.
    :type dic: dict
    :param depth: Current depth level.
    :type depth: int
    :return: String representation of the dictionary in "stylish" format.
    :rtype: str
    """

    lines = []
    indent = "    " * depth

    for key, value in sorted(dic.items()):
        lines.append(format_line(key, value, " ", depth))

    result = itertools.chain("{", lines, [indent + "}"])
    return "\n".join(result)
