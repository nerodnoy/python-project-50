def get_diff(file1, file2):
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


def add_node(key, node_type, old_value=None, new_value=None, children=None):
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
