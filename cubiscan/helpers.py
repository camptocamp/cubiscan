# Copyright 2019 Camptocamp SA
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)


def decode(value):
    return value.decode('ascii')


def extract_measure(value):
    value_str, error = base_extract(value)
    return (float(value_str), error)


def base_extract(value):
    """Extract the value and error if there are unprecise measurements."""
    acc_value = value[1:]
    error = None
    value_str = decode(acc_value)
    value_str = value_str.strip()
    first_char = value_str[0]
    if not first_char.isnumeric():
        if first_char == '_':
            error = 'low'
        elif first_char == '-':
            error = 'low_precision'
        elif first_char == '~':
            error = 'over'
        value_str = value_str[1:]
    return value_str, error


def dim_to_bool(value):
    value_str = decode(value)
    return value_str == 'M'


def extract_factor(value):
    value_str, error = base_extract(value)
    return int(value_str)


def dom_intl_to_bool(value):
    value_str = decode(value)
    return value_str == 'I'


def get_error(value):
    """Get more sensible description for errors."""
    # The chars are defined as capitals we will never be lowercase.
    value_str = decode(value)
    if value_str == 'C':
        return 'corner_sensor'
    elif value_str == 'M':
        return 'measure_error'
    elif value_str == 'Z':
        return 'zeroing_error'
    else:
        return 'unknown'


def ack_to_bool(value):
    value_str = decode(value)
    return value_str == 'A'
