import sys
from gendiff.cli import get_parser_args


def test_get_parser_args_with_plain_format():
    sys.argv = ['gendiff', '--format', 'plain', 'file1.json', 'file2.json']
    args = get_parser_args()
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'plain'


def test_get_parser_args_with_default_format():
    sys.argv = ['gendiff', 'file1.json', 'file2.json']
    args = get_parser_args()
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format is None


def test_get_parser_args_with_json_format():
    sys.argv = ['gendiff', '--format', 'json', 'file1.json', 'file2.json']
    args = get_parser_args()
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'json'

