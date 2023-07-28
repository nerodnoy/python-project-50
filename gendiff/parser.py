import argparse


def get_parser_args():
    parser = argparse.ArgumentParser(
        description="Generate diff between two files. Supported extensions: JSON/YAML/YML."
    )

    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)

    parser.add_argument(
        "-f", "--format",
        type=str,
        help="set format of output (stylish or plain)",
        choices=["stylish",
                 "plain"],
        default='stylish'
    )

    args = parser.parse_args()

    return args
