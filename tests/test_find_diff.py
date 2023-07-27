import pytest
from gendiff.find_diff import get_diff


def test_same_data():
    data1 = {"a": 1, "b": 2, "c": 3}
    data2 = {"a": 1, "b": 2, "c": 3}
    expected_result = "{\n    a: 1\n    b: 2\n    c: 3\n}"
    assert get_diff(data1, data2) == expected_result


def test_added_key():
    data1 = {"a": 1, "b": 2}
    data2 = {"a": 1, "b": 2, "c": 3}
    expected_result = "{\n    a: 1\n    b: 2\n  + c: 3\n}"
    assert get_diff(data1, data2) == expected_result


def test_removed_key():
    data1 = {"a": 1, "b": 2, "c": 3}
    data2 = {"a": 1, "b": 2}
    expected_result = "{\n    a: 1\n    b: 2\n  - c: 3\n}"
    assert get_diff(data1, data2) == expected_result


def test_changed_value():
    data1 = {"a": 1, "b": 2, "c": 3}
    data2 = {"a": 1, "b": 5, "c": 3}
    expected_result = "{\n    a: 1\n  - b: 2\n  + b: 5\n    c: 3\n}"
    assert get_diff(data1, data2) == expected_result
