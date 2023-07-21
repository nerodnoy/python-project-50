from gendiff.file_management import open_file
from gendiff.find_diff import get_diff


def generate_diff(file1, file2):
    file1 = open_file(file1)
    file2 = open_file(file2)

    diff = get_diff(file1, file2)
    
    return diff
