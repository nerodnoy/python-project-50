import pytest
from gendiff.find_diff import get_diff, add_node


def test_add_node():
    node = add_node('key', 'added', new_value='value')
    assert node == {'key': 'key', 'type': 'added', 'new_value': 'value'}

    node = add_node('key', 'removed', old_value='value')
    assert node == {'key': 'key', 'type': 'removed', 'old_value': 'value'}

    node = add_node('key', 'unchanged', old_value='value')
    assert node == {'key': 'key', 'type': 'unchanged', 'old_value': 'value'}

    node = add_node('key', 'updated', old_value='old_value', new_value='new_value')
    assert node == {'key': 'key', 'type': 'updated', 'old_value': 'old_value', 'new_value': 'new_value'}

    node = add_node('key', 'nested', children=[{'key': 'nested_key', 'type': 'added', 'new_value': 'nested_value'}])
    assert node == {'key': 'key', 'type': 'nested',
                    'children': [{'key': 'nested_key', 'type': 'added', 'new_value': 'nested_value'}]}


def test_get_diff():
    file1 = {
        "key1": "value1",
        "key2": "value2",
        "key3": {"nested_key": "nested_value"}
    }

    file2 = {
        "key1": "value1",
        "key3": {"nested_key": "modified_nested_value"},
        "key4": "value4"
    }

    diff = get_diff(file1, file2)
    assert diff == [
        {'key': 'key1', 'type': 'unchanged', 'old_value': 'value1'},
        {'key': 'key2', 'type': 'removed', 'old_value': 'value2'},
        {'key': 'key3', 'type': 'nested', 'children': [
            {'key': 'nested_key', 'type': 'updated', 'old_value': 'nested_value',
             'new_value': 'modified_nested_value'}]},
        {'key': 'key4', 'type': 'added', 'new_value': 'value4'}
    ]
