import pytest
from gendiff.find_diff import get_diff, add_node


def test_removed_node():
    node = add_node("key1", "removed", old_value="value1")
    assert node == {"key": "key1", "type": "removed", "old_value": "value1"}


def test_added_node():
    node = add_node("key2", "added", new_value="value2")
    assert node == {"key": "key2", "type": "added", "new_value": "value2"}


def test_updated_node():
    node = add_node("key3", "updated", old_value="value3", new_value="value4")
    assert node == {"key": "key3", "type": "updated", "old_value": "value3", "new_value": "value4"}


def test_nested_node():
    children = [{"key": "child1", "type": "removed", "old_value": "child_value1"}]
    node = add_node("key4", "nested", children=children)
    assert node == {"key": "key4", "type": "nested", "children": children}


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
