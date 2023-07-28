def convert_to_str(value):
    if isinstance(value, bool):
        converted = str(value).lower()
    elif value == "":
        converted = ""
    elif value is None:
        converted = "null"
    else:
        converted = str(value)

    return converted


def convert_to_str_or_complex(value):
    if isinstance(value, bool):
        converted = str(value).lower()
    elif isinstance(value, int):
        converted = str(value)
    elif isinstance(value, dict):
        converted = '[complex value]'
    elif value is None:
        converted = 'null'
    else:
        converted = f"'{str(value)}'"

    return converted
