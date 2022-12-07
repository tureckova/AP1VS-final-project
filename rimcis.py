"""
Závěrečný projekt skupiny Štefka Bobál Spurný do předmětu AP1VS.

.. include:: README.md
"""

import re
import sys

# Hodnoty Římských číslic a čísla, ke kterým korespondují
rn_chars = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
rn_chars_values = [1000, 500, 100, 50, 10, 5, 1]

# Regex který dokáže rozeznat symboly římských číslic a normální číslice
rx_only_rn = re.compile('^[IVXLCDM]+$')
rx_only_num = re.compile('^[1234567890]+$')


def generate_result(program_input):
    """
    Generate resulting string, given the input.

    Given a particular input in the form of a string, returns the converted
    value. Can detect whether it has recieved a Number input or a Roman
    Numeral input, and calls the required convertor function accordingly.

    :param program_input: The string input that the program recieves, which
    needs to be converted.

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
    ValueError: Input must only contain Roman Numerals, or only Numbers.
    """
    if type(program_input) not in [str]:
        raise TypeError('Value must be a string.')

    # Převede vstup na uppercase, aby byly symboly rozeznány v programu
    program_input = program_input.upper()

    # Pokud obsahuje vstup pouze římské symboly, proveď převedení z
    # římských symbolů na číslo
    if rx_only_rn.match(program_input) is not None:
        return convert_rn_to_num(program_input)

    # Pokud obsahuje pouze čísla, převeď z čísla na Římskou číslici
    elif rx_only_num.match(program_input) is not None:
        return convert_num_to_rn(int(program_input))

    else:
        raise ValueError('Input must only contain Roman Numerals, or only '
                         'Numbers.')


def convert_num_to_rn(input_num):
    """
    Convert Numbers to Roman Numerals.

    Given a particular Number, converts it to its corresponding Roman
    Numeral. Can identify whether the Number it has recieved falls into the
    range of valid Roman Numerals.

    :param input_num: The Number in the form of an int, which needs to be
    converted to a Roman Numeral.

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
        raise ValueError('Number is out of valid Roman Numeral range '
                         '(1-3999).')

    i = 0
    result_rn = ''

    # Dívá se na menší a menší symboly, jestli se nevlezou do zbytku čísla
    while i < len(rn_chars_values):

        # Předpona je symbol, který může být napsán před římský symbol, pro
        # znížení její hodnoty.
        prefix_index = 0
        prefix_val = 0

        # Podívá se, jaká předpona by mohla být použita pro toto číslo, pokud
        # by se samotný symbol do zbytku nevešel
        if i < len(rn_chars_values) - 1:

            prefix_index = i + (2 if i % 2 == 0 else 1)
            prefix_val = rn_chars_values[prefix_index]

        # Rozhodne se, jestli se dá od čísla odečíst hodnota daného symbolu
        if input_num >= rn_chars_values[i]:

            input_num -= rn_chars_values[i]
            result_rn += rn_chars[i]

        # pokud ne, tak se podívá, zda by se hodnota dala odečíst, kdyby byla
        # hodnota znížena pomocí předpony
        elif input_num >= rn_chars_values[i] - prefix_val:

            input_num -= rn_chars_values[i] - prefix_val
            result_rn += rn_chars[prefix_index] + rn_chars[i]

        # pokud ani to ne, tak přidá k 'i' 1 a opakuje celý proces se symbolem
        # s menší hodnotou
        else:
            i += 1

    return result_rn


def convert_rn_to_num(input_rn):
    """
    Convert Roman Numerals to Numbers.

    Given a particular Roman Numeral, converts it to its corresponding
    Number. Can identify whether the string it has recieved is a valid
    Roman Numeral, and return a custom error message if it isn't,
    detailing the problem.

    :param input_rn: The Roman Numeral in the form of a string, which needs
    to be converted to a Number.

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

    >>> convert_rn_to_num('MCMCMXIV')
    Traceback (most recent call last):
    ...
    ValueError: Symbol M cannot repeat after a prefix.

    >>> convert_rn_to_num('IXII')
    Traceback (most recent call last):
    ...
    ValueError: Lesser formating error during conversion. Did you mean XI?

    >>> convert_rn_to_num('XDMCL')
    Traceback (most recent call last):
    ...
    ValueError: This is not a correct Roman Numeral order.
    """
    if type(input_rn) not in [str]:
        raise TypeError('Input must be a string.')
    elif rx_only_rn.match(input_rn) is None:
        raise ValueError('Input contains non-Roman Numeral symbols.')

    # Použit pro finální porovnávací test integrity
    input_unaltered = input_rn

    i = 0
    result_num = 0

    # Hodnoty použity pro ujištění, že se symboly neoběvují v místech, kde
    # by neměli
    symbol_repeating_count = 0
    symbol_already_prefixed = False

    while i < len(rn_chars_values):

        prefix_index = 0
        prefix_char = ''

        if i < len(rn_chars_values) - 1:

            prefix_index = i + (2 if i % 2 == 0 else 1)
            prefix_char = rn_chars[prefix_index]

        # Pokud byl rozebrán celý vstup a nic z něho nezbývá, ukončí převádění
        if len(input_rn) < 1:
            break

        # proměnné uloží první dvě hodnoty ze vstupu (pokud má alespoň 2)
        first_char = str(input_rn[0])
        second_char = ''

        if len(input_rn) > 1:
            second_char = str(input_rn[1])

        # Pokud je první symbol očekávaný symbol, přičti jeho hodnotu k
        # výsledku, a odstraň tento symbol z inputu
        if first_char == rn_chars[i]:

            input_rn = input_rn[1:]
            result_num = result_num + rn_chars_values[i]
            symbol_repeating_count += 1

            # Pokud se symbol opakuje víc jak 3x po sobě, nebo pokud se
            # neopakovatelný symbol (V,L,D) ukáže více než 1x, je špatně
            if symbol_repeating_count > 3:
                raise ValueError(f'Symbol {rn_chars[i]} appears too many '
                                 f'times in a row.')

            elif i % 2 == 1 and symbol_repeating_count > 1:
                raise ValueError(f'Symbol {rn_chars[i]} can never repeat.')

            # Pokud se kterýkoliv symbol opakuje poté, co na něm byla použita
            # předpona, je špatně
            if symbol_already_prefixed:
                raise ValueError(f'Symbol {rn_chars[i]} cannot repeat after '
                                 f'a prefix.')

        # Pokud lze první symbol použít jako předponu před očekávaným
        # symbolem, a pokud je očekávaný symbol na druhém místě, lze odečíst
        # hodnotu očekávaného symbolu mínus hodnotu předpony. Tyto symboly
        # jsou poté odstraněny z inputu
        elif first_char == prefix_char and second_char == rn_chars[i]:
            input_rn = input_rn[2:]
            result_num = result_num + rn_chars_values[i] \
                - rn_chars_values[prefix_index]

            if symbol_already_prefixed:
                raise ValueError(f'Symbol {rn_chars[i]} cannot repeat after '
                                 f'a prefix.')

            symbol_already_prefixed = True

        # Pokud nelze nic jiného, tak se podívá, zda je následující symbol
        # ve správném pořadí oproti již porovnaných symbolech
        elif i < rn_chars.index(first_char):
            i += 1
            symbol_repeating_count = 0
            symbol_already_prefixed = False

        # pokud není ve správném pořadí, je input špatně
        else:
            raise ValueError('This is not a correct Roman Numeral order.')

    # Poslední možnost zachytit chybu. Pokud je převedeno číslo zpět do
    # římského, a nerovná se originálu, někde se nalézá chyba
    reference = convert_num_to_rn(result_num)
    if reference != input_unaltered:
        raise ValueError(f'Lesser formating error during conversion. Did you '
                         f'mean {reference}?')

    return result_num


if __name__ == '__main__':

    val = ""

    if len(sys.argv) > 1:
        val = sys.argv[1]
    else:
        val = input('Value: ')

    print(generate_result(val))

    if len(sys.argv) <= 1:
        input('Press Any Key To Exit ... ')
