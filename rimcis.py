"""Vzorový kód pro závěrečný projekt předmětu Ap1VS.

.. include:: README.md

Následuje ukázka vzorové funkce.
"""
import sys
import re
rn_chars = ["M", "D", "C", "L", "X", "V", "I"]
rn_maps_to = [1000, 500, 100, 50, 10, 5, 1]

rxRN = re.compile("^[IVXLCDM]+$")
rxNO = re.compile("^[1234567890]+$")


def compute(x):
    """Funkce počítá výsledek výrazu pro zadaný agrument x.

    :param x: Vstupní parametr x.
    :return: Vrací hodnotu výrazu pro vstupní parametr x.

    >>> compute(3)
    3
    """
    return 3


def convert_num_to_rn(number_input):

    i = 0
    rn_result = ""

    while i < len(rn_maps_to):

        decreaser_index = 0
        decreaser = 0

        if i < len(rn_maps_to) - 1:

            decreaser_index = i + (2 if i % 2 == 0 else 1)
            decreaser = rn_maps_to[decreaser_index]

        if number_input >= rn_maps_to[i]:

            number_input -= rn_maps_to[i]
            rn_result += rn_chars[i]

        elif number_input >= rn_maps_to[i] - decreaser:

            number_input -= rn_maps_to[i] - decreaser
            rn_result += rn_chars[decreaser_index] + rn_chars[i]

        else:
            i = i + 1

    return rn_result

def convert_rn_to_num(rn_input):

    i = 0
    number_result = 0

    while i < len(rn_maps_to):

        decreaser_char_index = 0
        decreaser_char = ""

        if i < len(rn_maps_to) - 1:

            decreaser_char_index = i + (2 if i % 2 == 0 else 1)
            decreaser_char = rn_chars[decreaser_char_index]
                        

        if len(rn_input) < 1:
            break

        first_char = str(rn_input[0])
        second_char = ""

        if len(rn_input) > 1:
            second_char = str(rn_input[1])

        if first_char == rn_chars[i]:
                        
            rn_input = rn_input[1:]
            number_result = number_result + rn_maps_to[i]
                        
        elif first_char == decreaser_char and second_char == rn_chars[i]:
            rn_input = rn_input[2:]
            number_result = number_result + rn_maps_to[i] - rn_maps_to[decreaser_char_index]
                        
        elif i < rn_chars.index(first_char):
            i = i + 1

        else:
            return -1


    return number_result 

if __name__ == '__main__':
    input = input("hodnota: ")
    if rxRN.match(input)!=None:
        print(convert_rn_to_num(input))

    if rxNO.match(input)!=None:
        print(convert_num_to_rn(int(input)))


