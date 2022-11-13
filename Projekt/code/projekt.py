from typing import List

"""Basic Converter that can convert between different numeral systems.

This converter can convert numbers from unary numeral system
and ending at the hexatridecimal numeral system.

Other numeral systems are basically useless because there is no
usage for them and there is not enough letters in
the latin alphabet for them to use.
"""

# Create a dictionary of the latin alphabet for numeral systems
# that have the base bigger than 10 -> 10: 'A', 11: 'B', .....,  35: 'Z'
keys: List[int] = range(10, 36)
values = [chr(i) for i in range(65, 91)]
letters_dict = dict(zip(keys, values))


def to_digits(number: int):
    """Convert number to a list of digits of the number."""
    digits = []

    while number > 0:
        digits.append(number % 10)
        number //= 10

    digits.reverse()
    return digits


def to_decimal(source_base: int, number: int, digits: List[int]):
    """Covert number from source_base to the number in decimal system."""
    decimal_number = 0

    if not digits:
        digits = to_digits(number)

    digits.reverse()
    for i in range(len(digits)):
        decimal_number += digits[i] * (source_base ** i)

    return decimal_number


def to_destination_base(destination_base: int, dec_num: int):
    """Convert number from decimal numeral system to number in dest_base."""
    mod_list = []

    # Unary numeral system is kinda unique so that´s why
    # it has different approach
    if destination_base == 1:
        mod_list = [1] * dec_num
        
    else:
        # Convert decimal number to the number in destination base
        # with the usage of modulo function.
        while dec_num > 0:
            mod_list.append(dec_num % destination_base)
            dec_num //= destination_base

        # If the numeral system is bigger than decimal system and lower
        # than heptatridecimal numeral system, than we might need to use
        # letters from the latin alphabet.
        if 10 < destination_base < 37:
            for i in range(0, len(mod_list)):
                if mod_list[i] > 9:
                    mod_list[i] = letters_dict[mod_list[i]]

    mod_list = [str(i) for i in mod_list]
    mod_list.reverse()
    return mod_list


def convert(source_base: int, destination_base: int, number: str) -> List[str]:
    """Convert number from src_base to dest_base by using other functions."""
    # If the source base is not equal to the decimal numeral system,
    # we have to convert the number from source base
    # to the decimal numeral system first.
    if source_base != 10:
        # Check if the number user inputted cointains only numbers
        if number.isdecimal():
            dec_num = to_decimal(source_base, int(number), [])

        else:
            # Convert number with letters in it to list of digits
            num_with_lett = [i for i in number]
            for i in range(len(num_with_lett)):
                # If the item on current index is not a digit from 0 - 10, 
                # use the appropriate number from letters_dict
                if not num_with_lett[i].isdecimal():
                    num_with_lett[i] = keys[values.index(num_with_lett[i])]

            digits = [int(i) for i in num_with_lett]
            dec_num = to_decimal(source_base, 0, digits)
    else:
        dec_num = int(number)

    res = to_destination_base(destination_base, dec_num)
    res = "".join(res)
    return res


# Ask the user from which numeral system to which
# numeral system they want the number to be converted.
src_base = int(input("Zadej číslem číselnou soustavu, "
                     "ze které chceš číslo převést: "))
dest_base = int(input("Zadej číslem číselnou soustavu, "
                      "do které chceš číslo převést: "))

# This Converter can only covert numbers if the destination base and
# source base is higher than 0 or lower than 37.
if 0 < dest_base < 37 and 0 < src_base < 37:
    # If the condition of the source and destination base is met, ask user
    # what the number they want to convert is.
    num = input(f"Zadej číslo které chceš převést z {src_base} soustavy "
                f"do {dest_base} soustavy: ")
    original_number = num

    result = convert(src_base, dest_base, num)
    print()
    print(f"Vámi zadané číslo {original_number} z {src_base} "
          f"soustavy se v {dest_base} soustavě zapisuje jako {result}.")
else:
    print()
    print("Převodce soustav nedokáže číslo převést mezi "
          "Vámi zadanými soustavami, prosím zkuste to "
          "znovu s jinými soustavami.")
