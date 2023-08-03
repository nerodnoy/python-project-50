import pytest
import json
from gendiff.generate_diff import generate_diff


def get_data_for_results(path):
    with open(path) as file:
        return file.read()


@pytest.mark.parametrize('path1, path2, expected',
                         [('tests/fixtures/json/file_simple1.json',
                           'tests/fixtures/json/file_simple2.json',
                           get_data_for_results(
                               'tests/fixtures/results/plain_simple.txt')),
                          ('tests/fixtures/yaml/file_simple1.yaml',
                           'tests/fixtures/yaml/file_simple2.yaml',
                           get_data_for_results(
                               'tests/fixtures/results/plain_simple.txt')),
                          ('tests/fixtures/json/file_nested1.json',
                           'tests/fixtures/json/file_nested2.json',
                           get_data_for_results(
                               'tests/fixtures/results/plain_nested.txt')),
                          ('tests/fixtures/yaml/file_nested1.yaml',
                           'tests/fixtures/yaml/file_nested2.yaml',
                           get_data_for_results(
                               'tests/fixtures/results/plain_nested.txt'))
                          ]
                         )
def test_generate_diff_plain(path1, path2, expected):
    assert generate_diff(path1, path2, 'plain') == expected


@pytest.mark.parametrize('path1, path2, expected',
                         [('tests/fixtures/json/file_simple1.json',
                           'tests/fixtures/json/file_simple2.json',
                           get_data_for_results(
                               'tests/fixtures/results/stylish_simple.txt')),
                          ('tests/fixtures/yaml/file_simple1.yaml',
                           'tests/fixtures/yaml/file_simple2.yaml',
                           get_data_for_results(
                               'tests/fixtures/results/stylish_simple.txt')),
                          # ('tests/fixtures/json/file_nested1.json',
                          #  'tests/fixtures/json/file_nested2.json',
                          #  get_data_for_results(
                          #      'tests/fixtures/results/stylish_nested.txt')),
                          # ('tests/fixtures/yaml/file_nested1.yaml',
                          #  'tests/fixtures/yaml/file_nested2.yaml',
                          #  get_data_for_results(
                          #      'tests/fixtures/results/stylish_nested.txt'))
                          ]
                         )
def test_generate_diff_stylish(path1, path2, expected):
    assert generate_diff(path1, path2, 'stylish') == expected


@pytest.mark.parametrize('path1, path2, expected',
                         [('tests/fixtures/json/file_simple1.json',
                           'tests/fixtures/json/file_simple2.json',
                           get_data_for_results(
                               'tests/fixtures/results/json_simple.txt')),
                          ('tests/fixtures/yaml/file_simple1.yaml',
                           'tests/fixtures/yaml/file_simple2.yaml',
                           get_data_for_results(
                               'tests/fixtures/results/json_simple.txt')),
                          ('tests/fixtures/json/file_nested1.json',
                           'tests/fixtures/json/file_nested2.json',
                           get_data_for_results(
                               'tests/fixtures/results/json_nested.txt')),
                          ('tests/fixtures/yaml/file_nested1.yaml',
                           'tests/fixtures/yaml/file_nested2.yaml',
                           get_data_for_results(
                               'tests/fixtures/results/json_nested.txt'))
                          ]
                         )
def test_generate_diff_json(path1, path2, expected):
    assert generate_diff(path1, path2, 'json') == expected
