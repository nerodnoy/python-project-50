import argparse


def get_parser_args():
    parser = argparse.ArgumentParser(
        description="Generate diff between two JSON and YAML/YML files."
    )

    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)

    parser.add_argument(
        "-f", "--format",
        type=str,
        help="set format of output",  # add (stylish, plain ... ) later
        choices=["stylish"],
        default='stylish'
    )

    args = parser.parse_args()

    return args
