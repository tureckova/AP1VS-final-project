"""Kód programu pro určení prvočíselnosti zadaných čísel.

.. include:: README.md

Následuje kód programu pro určení prvočíselnosti zadaných čísel.
"""
import random
def TestPrvociselnosti(x):
    """Funkce počítá zdali je zadané číslo prvočíslo.

    :param x: Vstupní parametr x.
    :return: Vrací textový řetězec s textem zdali je číslo prvočíslo.

    >>> TestPrvociselnosti(3)
    Jedná se o prvočíslo.
    >>> TestPrvociselnosti(8)
    Nejedná se o prvočíslo.
    >>> TestPrvociselnosti(True)
    Traceback (most recent call last):
    ...
    TypeError: X must be a number.
    """
    """Funkce počítá jestli je číslo prvočíslo nebo ne pomocí Miller-Rabinova testu."""
    if x == 2:
        return "Jedná se o prvočíslo."
    if x % 2 == 0 or x <= 1:
        return "Nejedná se o prvočíslo."
    s = 0
    d = x - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for i in range(10):
        a = random.randrange(2, x - 1)
        x0 = pow(a, d, x)
        if x0 == 1 or x0 == x - 1:
            continue
        for r in range(1, s):
            x0 = pow(x0, 2, x)
            if x0 == 1:
                return "Nejedná se o prvočíslo."
            if x0 == x - 1:
                a = 0
                break
        if a:
            return "Nejedná se o prvočíslo."
    return "Jedná se o prvočíslo."

if __name__ == '_main_':
    num = int(input('Zadej číslo k otestování:'))
    print(TestPrvociselnosti(num))
    print("Byla použita metoda Miller-Rabinova testu.")