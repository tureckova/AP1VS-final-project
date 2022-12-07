"""Python program that converts user input (in this case an integer in decimal numeral system) into other numeral systems."""

def number_system_converter(dec):
    """A function that converts decimal integer into binary, hexadecimal and octal systems."""
    
    if type(dec) not in [int]:
        raise TypeError("Type error. Input must be an integer.")
    if dec <= 0:
        raise ValueError("Value error. Input must be a positive number.")
    return ("Binary: " + bin(dec) + ", hexadecimal: " + hex(dec) + ", octal: " + oct(dec))
