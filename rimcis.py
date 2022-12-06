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
            i = i + 1

    return result_rn

def convert_rn_to_num(input_rn):

    i = 0
    result_num = 0

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

        #Pokud lze první symbol použít jako předponu před očekávaným symbolem, a pokud je očekávaný symbol na druhém místě
        elif first_char == prefix_char and second_char == rn_chars[i]:
            input_rn = input_rn[2:]
            result_num = result_num + rn_chars_values[i] - rn_chars_values[prefix_index]

        #Pokud nelze nic jiného, tak se podívá, zda je následující symbol ve správném pořadí oproti již porovnaných symbolech
        elif i < rn_chars.index(first_char):
            i = i + 1

        #pokud není ve správném pořadí, ERROR
        else:
            return -1


    return result_num 

if __name__ == '__main__':

    val = input("Value: ")

    if rx_only_rn.match(val)!=None:
        print(convert_rn_to_num(val))

    if rx_only_num.match(val)!=None:
        print(convert_num_to_rn(int(val)))

    input("Press Any Key To Exit ...")

