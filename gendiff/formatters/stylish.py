import itertools
from gendiff.formatters.converters import convert_to_str
from gendiff.constants import (
    TEMPLATE_NESTED,
    TEMPLATE_STYLISH
)


def create_stylish(diff):
    result = format_diff(diff)
    return result


def format_diff(data, depth=0):
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


def format_nested_node(node, indent, depth):
    nested_lines = format_diff(node["children"], depth + 1)
    return TEMPLATE_NESTED.format(indent, node["key"], nested_lines)


def format_single_node(node, indent, depth):
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


def format_line(key, value, sign, depth):
    indent = "    " * depth
    lines = []

    if isinstance(value, dict):
        lines.append(TEMPLATE_STYLISH.format(
            indent, sign, key, format_dict(value, depth + 1)))
    else:
        lines.append(TEMPLATE_STYLISH.format(
            indent, sign, key, convert_to_str(value)))

    return "\n".join(lines)


def format_dict(dic, depth):
    lines = []
    indent = "    " * depth

    for key, value in sorted(dic.items()):
        lines.append(format_line(key, value, " ", depth))

    result = itertools.chain("{", lines, [indent + "}"])
    return "\n".join(result)
