from gendiff.formatters.stylish import create_stylish as stylish
from gendiff.formatters.plain import create_plain as plain


def format_output(diff, format):
    if format == 'stylish':
        return stylish(diff)
    if format == 'plain':
        return plain(diff)
