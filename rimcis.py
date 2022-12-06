"""Vzorový kód pro závěrečný projekt předmětu Ap1VS.

.. include:: README.md

Následuje ukázka vzorové funkce.
"""
import sys
import re

rn_chars = ["M", "D", "C", "L", "X", "V", "I"]
rn_chars_values = [1000, 500, 100, 50, 10, 5, 1]

rx_only_rn = re.compile("^[IVXLCDM]+$")
rx_only_num = re.compile("^[1234567890]+$")


def compute(x):
    """Funkce počítá výsledek výrazu pro zadaný agrument x.

    :param x: Vstupní parametr x.
    :return: Vrací hodnotu výrazu pro vstupní parametr x.

    >>> compute(3)
    3
    """
    return 3


def convert_num_to_rn(input_num):

    if input_num < 1 or input_num > 3999:
        raise ValueError("Number is out of valid Roman Numeral range (1-3999)")

    i = 0
    result_rn = ""

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
    input_unaltered = input_rn
    i = 0
    result_num = 0
    symbol_repeating_count = 0
    symbol_already_prefixed = False

    while i < len(rn_chars_values):

        prefix_index = 0
        prefix_char = ""

        if i < len(rn_chars_values) - 1:

            prefix_index = i + (2 if i % 2 == 0 else 1)
            prefix_char = rn_chars[prefix_index]

        #pokud ze vstupu už nic nezbývá
        if len(input_rn) < 1:
            break

        #proměnné uloží první dvě hodnoty ze vstupu (pokud má alespoň 2 hodnoty)
        first_char = str(input_rn[0])
        second_char = ""

        if len(input_rn) > 1:
            second_char = str(input_rn[1])

        #Pokud je první symbol očekávaný symbol
        if first_char == rn_chars[i]:

            input_rn = input_rn[1:]
            result_num = result_num + rn_chars_values[i]
            symbol_repeating_count += 1

            #Pokud se symbol opakuje víc jak 3x po sobě, nebo pokud se neopakovatelný symbol (V,L,D) ukáže více než 1x
            if symbol_repeating_count > 3:
                raise ValueError(f"Symbol {rn_chars[i]} appears too many times in a row.")

            elif i % 2 == 1 and symbol_repeating_count > 1:
                raise ValueError(f"Symbol {rn_chars[i]} can never repeat.")

            #Pokud už bylo před symbolem něco jiného
            if symbol_already_prefixed:
                raise ValueError(f"Symbol {rn_chars[i]} cannot repeat after a prefix.")

        #Pokud lze první symbol použít jako předponu před očekávaným symbolem, a pokud je očekávaný symbol na druhém místě
        elif first_char == prefix_char and second_char == rn_chars[i]:
            input_rn = input_rn[2:]
            result_num = result_num + rn_chars_values[i] - rn_chars_values[prefix_index]

            if symbol_already_prefixed:
                raise ValueError(f"Symbol {rn_chars[i]} cannot repeat after a prefix.")

            symbol_already_prefixed = True

        #Pokud nelze nic jiného, tak se podívá, zda je následující symbol ve správném pořadí oproti již porovnaných symbolech
        elif i < rn_chars.index(first_char):
            i += 1
            symbol_repeating_count = 0
            symbol_already_prefixed = False

        #pokud není ve správném pořadí, ERROR
        else:
            raise ValueError("This is not a correct Roman Numeral order.") #nebo type error?

    #Poslední možnost zachytit chybu. Pokud je převedeno číslo zpět do římského, a nerovná se originálu, tak je originální římské číslo špatně formátované
    reference = convert_num_to_rn(result_num)
    if reference != input_unaltered:
        raise ValueError(f"Lesser formating error arose during conversion. Did you mean {reference}?")

    return result_num

def generate_result(program_input):

    if type(val) not in [str]:
        raise TypeError("Value must be a string.")

    program_input = program_input.upper()

    if rx_only_rn.match(program_input) is not None:
        return convert_rn_to_num(program_input)

    elif rx_only_num.match(program_input) is not None:
        return convert_num_to_rn(int(program_input))

    else:
        raise ValueError("Input must contain only Roman Numerals, or only Numbers.") #nebo type error?


if __name__ == '__main__':

    val = input("Value: ")

    print(generate_result(val))

    input("Press Any Key To Exit ...")

