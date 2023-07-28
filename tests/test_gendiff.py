import pytest
from gendiff.generate_diff import generate_diff


def get_data_for_results(path):
    with open(path) as file:
        return file.read()


@pytest.mark.parametrize('path1, path2, expected',
                         [('tests/fixtures/json/file1.json',
                           'tests/fixtures/json/file2.json',
                           get_data_for_results(
                               'tests/fixtures/results/result_json.txt')),
                          ('tests/fixtures/yaml/file1.yaml',
                           'tests/fixtures/yaml/file2.yaml',
                           get_data_for_results(
                               'tests/fixtures/results/result_yaml.txt')),
                          # ('tests/fixtures/json/file1_nested.json',
                          #  'tests/fixtures/json/file2_nested.json',
                          #  get_data_for_results(
                          #      'tests/fixtures/results/result_pathfile_json.txt')),
                          # ('tests/fixtures/yaml/file1_nested.yaml',
                          #  'tests/fixtures/yaml/file2_nested.yaml',
                          #  get_data_for_results(
                          #      'tests/fixtures/results/result_pathfile_yaml.txt'))
                          ]
                         )
def test_generate_diff_stylish(path1, path2, expected):
    assert generate_diff(path1, path2) == expected.strip()
