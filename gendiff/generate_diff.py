from gendiff.file_management import open_file
from gendiff.find_diff import get_diff
from gendiff.formatters.format_ouput import format_output


def generate_diff(file1, file2, format='stylish'):
    file1 = open_file(file1)
    file2 = open_file(file2)

    diff = get_diff(file1, file2)

    formatted_diff = format_output(diff, format)

    return formatted_diff
