from gendiff.formatters.converters import convert_to_str_or_complex as converter
from gendiff.constants import (
    TEMPLATE_PLAIN_ADDED,
    TEMPLATE_PLAIN_REMOVED,
    TEMPLATE_PLAIN_UPDATED,
    TEMPLATE_PLAIN_PATH
)


def create_plain(diff: list, source: str = '') -> str:
    """
    Create the difference tree in "plain" format.

    :param diff: Difference tree.
    :param source: A path to current node.
    :return: A string of difference in "plain" format.
    """

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


def create_single_node(node: dict, path: str) -> str:
    """
    Create a single node representation in "plain" format.

    :param node: The node representing a difference.
    :type node: dict
    :param path: The path to the current node.
    :type path: str
    :return: A string representing the difference for the node in "plain" format
    :rtype: str
    """

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


def create_nested_node(node: dict, path: str) -> str:
    """
    Create a nested node representation in "plain" format.

    :param node: The node representing a nested difference.
    :type node: dict
    :param path: The path to the current node.
    :type path: str
    :return: A string representation of the nested difference in "plain" format.
    :rtype: str
    """

    nested_lines = create_plain(node["children"], path)

    return nested_lines
