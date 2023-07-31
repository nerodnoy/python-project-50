import json


def create_json(diff: dict) -> str:
    """
    Create the difference tree in "json" format.

    This function takes the difference tree as input and converts
    it into a JSON-formatted string
    with indentation for better readability.

    :param diff: The difference tree as a dictionary.
    :type diff: dict
    :return: A string representation of the difference tree in "json" format.
    :rtype: str
    """

    result = json.dumps(format_json(diff), indent=4)
    return result


def format_json(data) -> str:
    """
    Recursively format the difference tree into a dictionary.

    This function iterates through the difference tree nodes and
    returns a string representation of the differences.
    Each node's key is associated with its type and relevant
    values like old_value, new_value, or nested differences.

    :param data: The difference node or subtree as a list of dictionaries.
    :type data: list
    :return: A string representation of the difference.
    :rtype: str
    """

    diff_json = {}
    data.sort(key=lambda node: node['key'])

    for node in data:
        node_type = node['type']

        if node_type in ['removed', 'unchanged']:
            diff_json[node['key']] = {'value': node['old_value']}

        elif node_type == 'added':
            new_value = node.get('new_value', None)
            diff_json[node['key']] = {'value': new_value}

        elif node_type == 'updated':
            old_value = node.get('old_value', None)
            new_value = node.get('new_value', None)
            diff_json[
                node['key']] = {'value': old_value, 'new value': new_value}

        elif node_type == 'nested':
            diff_json[node['key']] = {'value': format_json(node['children'])}

        diff_json[node['key']]['type'] = node_type

    return diff_json
