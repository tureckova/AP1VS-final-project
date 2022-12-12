"""Kód programu pro určení prvočíselnosti zadaných čísel.

.. include:: README.md

Následuje kód programu pro určení prvočíselnosti zadaných čísel.
"""
import random
def TestPrvociselnosti(x):
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