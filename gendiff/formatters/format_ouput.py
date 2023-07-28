from gendiff.formatters.stylish import create_stylish


def format_output(diff, format):
    if format == 'stylish':
        return create_stylish(diff)
    else:
        pass
