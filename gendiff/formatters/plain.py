from gendiff.formatters.converters import convert_to_str_or_complex as converter
from gendiff.constants import (
    TEMPLATE_PLAIN_ADDED,
    TEMPLATE_PLAIN_REMOVED,
    TEMPLATE_PLAIN_UPDATED,
    TEMPLATE_PLAIN_PATH
)


def create_plain(diff, source=""):
    lines = []
    diff.sort(key=lambda node: node["key"])

    for node in diff:
        if source:
            path = TEMPLATE_PLAIN_PATH.format(source, node["key"])
        else:
            path = node["key"]

        if node["type"] == "nested":
            lines.append(create_nested_node(node, path))
        else:
            lines.extend(create_single_node(node, path))

    result = "\n".join(lines)

    return result


def create_single_node(node, path):
    lines = []
    if node["type"] == "removed":
        lines.append(TEMPLATE_PLAIN_REMOVED.format(path))
    elif node["type"] == "added":
        new_value = node.get("new_value", None)
        lines.append(TEMPLATE_PLAIN_ADDED.format(path, converter(new_value)))
    elif node["type"] == "updated":
        old_value = node.get("old_value", None)
        new_value = node.get("new_value", None)
        lines.append(
            TEMPLATE_PLAIN_UPDATED.format(
                path, converter(old_value), converter(new_value))
        )

    return lines


def create_nested_node(node, path):
    nested_lines = create_plain(node["children"], path)

    return nested_lines
