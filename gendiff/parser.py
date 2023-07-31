import argparse


def get_parser_args():
    """
    Parse command-line arguments for generating the difference report.

    This function sets up an ArgumentParser to handle command-line arguments.
    It defines the required positional arguments for the paths to the first
    and second files to compare. Additionally, it allows specifying an
    optional argument to choose the output format of the difference report.


    Parameters:
        - first_file: Path to the first file for comparison.
        - second_file: Path to the second file for comparison.
        - format: Format for output (e.g., default='stylish', 'plain', 'json').

    :return: Parsed input values (argparse arguments)
    """

    parser = argparse.ArgumentParser(
        description="Generate diff between two files. "
                    "Supported extensions: JSON/YAML/YML."
    )

    parser.add_argument("first_file", type=str, help='path/to/the/first/file')
    parser.add_argument("second_file", type=str, help='path/to/the/second/file')

    parser.add_argument(
        "-f", "--format",
        type=str,
        help="set format of output stylish, plain or json",
        choices=["stylish",
                 "plain",
                 "json"],
        default='stylish'
    )

    args = parser.parse_args()

    return args
