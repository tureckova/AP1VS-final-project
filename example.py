"""Vzorový kód pro závěrečný projekt předmětu Ap1VS.

.. include:: README.md

Následuje ukázka vzorové funkce.
"""

            # if i = 2 that indicates a new word
            if i == 2 :

def compute(x):
    """Funkce počítá výsledek výrazu pro zadaný agrument x.

    :param x: Vstupní parametr x.
    :return: Vrací hodnotu výrazu pro vstupní parametr x.

    >>> compute(3)
    3
    """
    x2 = x * x
    return x2 - 2 * x

# Hard-coded driver function to run the program
def main():
    message = "GEEKS-FOR-GEEKS"
    result = encrypt(message.upper())
    print (result)

if __name__ == '__main__':
    num = int(input('Insert a number:'))
    print(compute(num))
