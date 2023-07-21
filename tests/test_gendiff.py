import pytest
import json
from gendiff.generate_diff import generate_diff


def get_data_for_results(path):
    with open(path) as opened:
        file = opened.read()
    return file


@pytest.mark.parametrize('path1, path2, expected', [('tests/fixtures/json/file1.json',
                                                     'tests/fixtures/json/file2.json',
                                                     get_data_for_results(
                                                         'tests/fixtures/results/result_json.txt'))])
def test_generate_diff(path1, path2, expected):
    assert generate_diff(path1, path2) == expected.strip()



