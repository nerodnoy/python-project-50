from gendiff.generate_diff import generate_diff
from gendiff.parser import get_parser_args


def main():
    args = get_parser_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
