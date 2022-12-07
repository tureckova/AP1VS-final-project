"""Python program that converts decimal integer into various number systems."""


def number_system_converter(dec):
    """Convert decimal int into binary, hexadecimal and octal systems."""
    if type(dec) not in [int]:
        raise TypeError("Type error. Input must be an integer.")
    if dec <= 0:
        raise ValueError("Value error. Input must be a positive number.")
    return ("bin: " + bin(dec) + ", hex: " + hex(dec) + ", oct: " + oct(dec))
