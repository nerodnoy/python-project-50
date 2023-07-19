import argparse
from gendiff.diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Generate diff between two JSON files.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    parser.add_argument('-f', '--format', help="set format of output")

    args = parser.parse_args()
    file1_path = args.first_file
    file2_path = args.second_file

    diff = generate_diff(file1_path, file2_path)
    print(diff)


if __name__ == '__main__':
    main()
