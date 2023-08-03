from gendiff.file_management import open_file
from gendiff.find_diff import get_diff
from gendiff.formatters.format_ouput import format_output


def generate_diff(file1: str, file2: str, format: str = 'stylish') -> str:
    """
    Generate a difference report between two files.

    This function takes two file paths as input and compares the content of the
    files to generate a difference report. It loads the data from the files,
    finds the difference between the data, and then formats the difference
    using the specified output format (e.g., 'stylish', 'plain', 'json').

    :param file1: The path to the first file.
    :type file1: str
    :param file2: The path to the second file.
    :type file2: str
    :param format: The output format for the difference report
                   (default is 'stylish').
    :type format: str
    :return: A string representation of the difference report.
    :rtype: str
    """

    file1 = open_file(file1)
    file2 = open_file(file2)

    diff = get_diff(file1, file2)

    formatted_diff = format_output(diff, format)

    return formatted_diff
