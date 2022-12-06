"""
Závěrečný projekt skupiny Daniel Štefka, Martin Bobál, František Spurný, do předmětu AP1VS.

.. include:: README.md
"""

import re

rn_chars = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
rn_chars_values = [1000, 500, 100, 50, 10, 5, 1]

rx_only_rn = re.compile('^[IVXLCDM]+$')
rx_only_num = re.compile('^[1234567890]+$')

def convert_num_to_rn(input_num):
    """
    Given a particular Numeral, converts it to its corresponding Roman Numeral. Can identify whether the Numeral it has
    recieved falls into the range of valid Roman Numerals.

    :param input_num: The Numeral in the form of an int, which needs to be converted to a Roman Numeral.

    Sample usage:
    >>> convert_num_to_rn(1)
    'I'
    >>> convert_num_to_rn(1000)
    'M'
    >>> convert_num_to_rn(3999)
    'MMMCMXCIX'
    >>> convert_num_to_rn(36)
    'XXXVI'
    >>> convert_num_to_rn(254)
    'CCLIV'
    >>> convert_num_to_rn(1847)
    'MDCCCXLVII'
    >>> convert_num_to_rn(2840)
    'MMDCCCXL'
    >>> convert_num_to_rn(16.8)
    Traceback (most recent call last):
    ...
    TypeError: Input must be an integer.
    >>> convert_num_to_rn(7051)
    Traceback (most recent call last):
    ...
    ValueError: Number is out of valid Roman Numeral range (1-3999).
    """

    if type(input_num) not in [int]:
        raise TypeError('Input must be an integer.')

    if input_num < 1 or input_num > 3999:
        raise ValueError('Number is out of valid Roman Numeral range (1-3999).')

    i = 0
    result_rn = ''

    # Dokud nejsou projety všechny možné symboly
    while i < len(rn_chars_values):

        prefix_index = 0
        prefix_val = 0

        #IF se podívá, jaká předpona by mohla být použita pro toto číslo, kdyby se zde celá hodnota symbolu na pozici 'i' nevešla
        if i < len(rn_chars_values) - 1:

            prefix_index = i + (2 if i % 2 == 0 else 1)
            prefix_val = rn_chars_values[prefix_index]

        #IF se rozhodne, jestli se dá od čísla odečíst hodnota symbolu na pozici 'i'
        if input_num >= rn_chars_values[i]:

            input_num -= rn_chars_values[i]
            result_rn += rn_chars[i]

        #pokud ne, tak se podívá, zda by se zde toto číslo vešlo, kdyby od něj byla odečtena předpona
        elif input_num >= rn_chars_values[i] - prefix_val:

            input_num -= rn_chars_values[i] - prefix_val
            result_rn += rn_chars[prefix_index] + rn_chars[i]

        #pokud ani to ne, tak přidá k 'i' 1 a dívá se od znova z této pozice
        else:
            i += 1

    return result_rn


def convert_rn_to_num(input_rn):
    """
    Given a particular Roman Numeral, converts it to its corresponding Numeral. Can identify whether the string it has
    recieved is a valid Roman Numeral, and return a custom error message if it isn't; detailing the problem.

    :param input_rn: The Roman Numeral in the form of a string, which needs to be converted to a Numeral.

    Sample usage:
    >>> convert_rn_to_num('I')
    1
    >>> convert_rn_to_num('M')
    1000
    >>> convert_rn_to_num('MMMCMXCIX')
    3999
    >>> convert_rn_to_num('LXVIII')
    68
    >>> convert_rn_to_num('CMXCIX')
    999
    >>> convert_rn_to_num('MCMLXXXIV')
    1984
    >>> convert_rn_to_num('MMMDXLVIII')
    3548
    >>> convert_rn_to_num(13)
    Traceback (most recent call last):
    ...
    TypeError: Input must be a string.
    >>> convert_rn_to_num('MMCBXIAA')
    Traceback (most recent call last):
    ...
    ValueError: Input contains non-Roman Numeral symbols.
    >>> convert_rn_to_num('MCXXXXIV')
    Traceback (most recent call last):
    ...
    ValueError: Symbol X appears too many times in a row.
    >>> convert_rn_to_num('MDDLVII')
    Traceback (most recent call last):
    ...
    ValueError: Symbol D can never repeat.
    >>> convert_rn_to_num('CIXXVII')
    Traceback (most recent call last):
    ...
    ValueError: Symbol X cannot repeat after a prefix.
    >>> convert_rn_to_num('IXII')
    Traceback (most recent call last):
    ...
    ValueError: Lesser formating error arose during conversion. Did you mean XI?
    >>> convert_rn_to_num('XDMCL')
    Traceback (most recent call last):
    ...
    ValueError: This is not a correct Roman Numeral order.
    """

    if type(input_rn) not in [str]:
        raise TypeError('Input must be a string.')
    elif rx_only_rn.match(input_rn) is None:
        raise ValueError('Input contains non-Roman Numeral symbols.')

    input_unaltered = input_rn
    i = 0
    result_num = 0
    symbol_repeating_count = 0
    symbol_already_prefixed = False

    while i < len(rn_chars_values):

        prefix_index = 0
        prefix_char = ''

        if i < len(rn_chars_values) - 1:

            prefix_index = i + (2 if i % 2 == 0 else 1)
            prefix_char = rn_chars[prefix_index]

        #pokud ze vstupu už nic nezbývá
        if len(input_rn) < 1:
            break

        #proměnné uloží první dvě hodnoty ze vstupu (pokud má alespoň 2 hodnoty)
        first_char = str(input_rn[0])
        second_char = ''

        if len(input_rn) > 1:
            second_char = str(input_rn[1])

        #Pokud je první symbol očekávaný symbol
        if first_char == rn_chars[i]:

            input_rn = input_rn[1:]
            result_num = result_num + rn_chars_values[i]
            symbol_repeating_count += 1

            #Pokud se symbol opakuje víc jak 3x po sobě, nebo pokud se neopakovatelný symbol (V,L,D) ukáže více než 1x
            if symbol_repeating_count > 3:
                raise ValueError(f'Symbol {rn_chars[i]} appears too many times in a row.')

            elif i % 2 == 1 and symbol_repeating_count > 1:
                raise ValueError(f'Symbol {rn_chars[i]} can never repeat.')

            #Pokud už bylo před symbolem něco jiného
            if symbol_already_prefixed:
                raise ValueError(f'Symbol {rn_chars[i]} cannot repeat after a prefix.')

        #Pokud lze první symbol použít jako předponu před očekávaným symbolem, a pokud je očekávaný symbol na druhém místě
        elif first_char == prefix_char and second_char == rn_chars[i]:
            input_rn = input_rn[2:]
            result_num = result_num + rn_chars_values[i] - rn_chars_values[prefix_index]

            if symbol_already_prefixed:
                raise ValueError(f'Symbol {rn_chars[i]} cannot repeat after a prefix.')

            symbol_already_prefixed = True

        #Pokud nelze nic jiného, tak se podívá, zda je následující symbol ve správném pořadí oproti již porovnaných symbolech
        elif i < rn_chars.index(first_char):
            i += 1
            symbol_repeating_count = 0
            symbol_already_prefixed = False

        #pokud není ve správném pořadí, ERROR
        else:
            raise ValueError('This is not a correct Roman Numeral order.')

    #Poslední možnost zachytit chybu. Pokud je převedeno číslo zpět do římského, a nerovná se originálu, tak je originální římské číslo špatně formátované
    reference = convert_num_to_rn(result_num)
    if reference != input_unaltered:
        raise ValueError(f'Lesser formating error arose during conversion. Did you mean {reference}?')

    return result_num

def generate_result(program_input):
    """
    Given a particular input in the form of a string, returns the converted value. Can detect whether it has recieved a
    Numeral input or a Roman Numeral input, and calls the required convertor function accordingly.

    :param program_input: The string input that the program recieves, which needs to be converted.

    Sample usage:
    >>> generate_result('XVI')
    16
    >>> generate_result('16')
    'XVI'
    >>> generate_result(16)
    Traceback (most recent call last):
    ...
    TypeError: Value must be a string.
    >>> generate_result(True)
    Traceback (most recent call last):
    ...
    TypeError: Value must be a string.
    >>> generate_result('IV80_plus3')
    Traceback (most recent call last):
    ...
    ValueError: Input must contain only Roman Numerals, or only Numbers.
    """

    if type(program_input) not in [str]:
        raise TypeError('Value must be a string.')

    program_input = program_input.upper()

    if rx_only_rn.match(program_input) is not None:
        return convert_rn_to_num(program_input)

    elif rx_only_num.match(program_input) is not None:
        return convert_num_to_rn(int(program_input))

    else:
        raise ValueError('Input must contain only Roman Numerals, or only Numbers.')


if __name__ == '__main__':

    val = input('Value: ')

    print(generate_result(val))

    input('Press Any Key To Exit ... ')

