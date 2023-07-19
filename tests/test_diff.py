import json
import pytest
from gendiff.diff import generate_diff

def test_generate_diff_with_equal_json_files(tmp_path):
    data = {'key1': 42, 'key2': 'value'}
    filepath1 = tmp_path / 'file1.json'
    filepath2 = tmp_path / 'file2.json'
    with open(filepath1, 'w') as file1, open(filepath2, 'w') as file2:
        json.dump(data, file1)
        json.dump(data, file2)

    expected_diff = '{\n    key1: 42\n    key2: value\n}'
    assert generate_diff(filepath1, filepath2) == expected_diff

def test_generate_diff_with_different_json_files(tmp_path):
    data1 = {'key1': 42, 'key2': 'value1'}
    data2 = {'key2': 'value2', 'key3': [1, 2, 3]}
    filepath1 = tmp_path / 'file1.json'
    filepath2 = tmp_path / 'file2.json'
    with open(filepath1, 'w') as file1, open(filepath2, 'w') as file2:
        json.dump(data1, file1)
        json.dump(data2, file2)

    expected_diff = (
        '{\n'
        '  - key1: 42\n'
        '  - key2: value1\n'
        '  + key2: value2\n'
        '  + key3: [1, 2, 3]\n'
        '}'
    )
    assert generate_diff(filepath1, filepath2) == expected_diff

def test_generate_diff_with_missing_files():
    with pytest.raises(FileNotFoundError):
        generate_diff('non_existent_file.json', 'another_non_existent_file.json')
