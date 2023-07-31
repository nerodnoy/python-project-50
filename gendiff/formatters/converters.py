def convert_to_str(value) -> str:
    """
    Convert any value to a string representation.

    This function takes a value of any format and converts it to its string
    representation.

    :param value: The value to be converted to a string.
    :type value: any
    :return: The string representation of the value.
    :rtype: str
    """

    if isinstance(value, bool):
        converted = str(value).lower()
    elif value == "":
        converted = ""
    elif value is None:
        converted = "null"
    else:
        converted = str(value)

    return converted


def convert_to_str_or_complex(value) -> str:
    """
    Convert a value to a string or [complex value] if the value is a dictionary.

    This function converts a value to its string representation, or if the value
    is a dictionary, returns the string '[complex value]'. If the value is None,
    it returns the string 'null'.

    :param value: The value to be converted.
    :type value: any
    :return: The string representation of the value or '[complex value]'
             if the value is a dictionary, or 'null' if the value is None.
    :rtype: str
    """

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
