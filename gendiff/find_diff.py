def get_diff(file1: dict, file2: dict) -> list:
    """
    Compare two dictionaries and generate a difference tree.

    This function takes two dictionaries as input and compares their keys and
    values to identify differences between them. It returns a list representing
    a difference tree, where each node contains information about the key,
    type of difference (added, removed, unchanged, updated, or nested), and
    relevant values for the corresponding difference type.

    :param file1: The first dictionary to compare.
    :type file1: dict
    :param file2: The second dictionary to compare.
    :type file2: dict
    :return: A list representing the difference tree.
    :rtype: list
    """

    keys = sorted(set(file1.keys()) | set(file2.keys()))
    tree = []

    for key in keys:
        if key in file1 and key not in file2:
            node = add_node(key, "removed", old_value=file1[key])

        elif key not in file1 and key in file2:
            node = add_node(key, "added", new_value=file2[key])

        elif file1[key] == file2[key]:
            node = add_node(key, "unchanged", old_value=file1[key])

        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            child = get_diff(file1[key], file2[key])
            node = add_node(key, "nested", children=child)

        else:
            node = add_node(
                key, "updated", new_value=file2[key], old_value=file1[key]
            )

        tree.append(node)

    return tree


def add_node(
    key: str,
    node_type: str,
    old_value=None,
    new_value=None,
    children=None
) -> dict:
    """
    Create a difference tree node.

    This function creates a node for the difference tree, representing a
    difference between two keys in the dictionaries being compared. The node
    contains information about the key, the type of difference (added,
    removed, unchanged, updated, or nested), and relevant values for the
    corresponding difference type.

    :param key: The key representing the difference.
    :type key: str
    :param node_type: The type of difference (added, removed, unchanged,
                      updated, or nested).
    :type node_type: str
    :param old_value: The old value associated with the key (optional).
    :type old_value: any
    :param new_value: The new value associated with the key (optional).
    :type new_value: any
    :param children: The nested difference tree for a nested difference
                     (optional).
    :type children: list
    :return: A dictionary representing the difference tree node.
    :rtype: dict
    """
    node = {
        "key": key,
        "type": node_type,
    }

    if old_value is not None:
        node["old_value"] = old_value

    if new_value is not None:
        node["new_value"] = new_value

    if children:
        node["children"] = children

    return node
