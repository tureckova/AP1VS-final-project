"""Python program that converts decimal integer into various number systems."""


def number_system_converter(dec):
    """Convert decimal int into binary, hexadecimal and octal systems.

    :param dec: Parameter of the converter function (int)

    Sample usage:
    >>> number_system_converter(0)
    Traceback (most recent call last):
    ...
    ValueError: Value error. Input must be a positive number.
    >>> number_system_converter(-7)
    Traceback (most recent call last):
    ...
    ValueError: Value error. Input must be a positive number.
    >>> number_system_converter(13)
    'bin: 0b1101, hex: 0xd, oct: 0o15'
    >>> number_system_converter(True)
    Traceback (most recent call last):
    ...
    TypeError: Type error. Input must be an integer.
    >>> number_system_converter(25.67)
    Traceback (most recent call last):
    ...
    TypeError: Type error. Input must be an integer.
    >>> number_system_converter("abcd")
    Traceback (most recent call last):
    ...
    TypeError: Type error. Input must be an integer.
    """
    if type(dec) not in [int]:
        raise TypeError("Type error. Input must be an integer.")
    if dec <= 0:
        raise ValueError("Value error. Input must be a positive number.")
    return ("bin: " + bin(dec) + ", hex: " + hex(dec) + ", oct: " + oct(dec))
