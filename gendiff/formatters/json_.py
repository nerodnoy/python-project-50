import json


def create_json(diff):
    result = json.dumps(format_json(diff), indent=4)
    return result


def format_json(data):
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
