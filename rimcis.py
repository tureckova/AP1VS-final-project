"""Vzorový kód pro závěrečný projekt předmětu Ap1VS.

.. include:: README.md

Následuje ukázka vzorové funkce.
"""

rn_chars = ["M", "D", "C", "L", "X", "V", "I"]
rn_maps_to = [1000, 500, 100, 50, 10, 5, 1]

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

if __name__ == '__main__':

    num = int(input('Insert a number:'))
    print(convert_num_to_rn(num))

