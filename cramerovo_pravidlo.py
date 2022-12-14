"""
Závěrečný projekt z předmětu AP1VS.

Projekt: Cramerovo pravidlo
Autoři: Ondřej Kraus, Michal Mudrák, Roman Kukumberg
Hlavní kód projektu cramerovo pravidlo
"""


def cramer_rule(a1, b1, c1, d1, a2, b2, c2, d2, a3, b3, c3, d3):
    """
    Vypocet sustavy linearnych rovnic pomocou Cramerovho pravidla.

    Zadanie hodnot neznamych.
    :param a1: Vstupní parametr souřadnice a11,
    :param b1: Vstupní parametr souřadnice a12,
    :param c1: Vstupní parametr souřadnice a13,
    :param d1: Vstupní parametr,
    :param a2: Vstupní parametr souřadnice a21,
    :param b2: Vstupní parametr souřadnice a22,
    :param c2: Vstupní parametr souřadnice a23,
    :param d2: Vstupní parametr,
    :param a3: Vstupní parametr souřadnice a31,
    :param b3: Vstupní parametr souřadnice a32,
    :param c3: Vstupní parametr souřadnice a33,
    :param d3: Vstupní parametr
    """
    if (type(a1) not in [int, float] or
            type(b1) not in [int, float] or
            type(c1) not in [int, float] or
            type(d1) not in [int, float] or
            type(a2) not in [int, float] or
            type(b2) not in [int, float] or
            type(c2) not in [int, float] or
            type(d2) not in [int, float] or
            type(a3) not in [int, float] or
            type(b3) not in [int, float] or
            type(c3) not in [int, float] or
            type(d3) not in [int, float]):
        raise TypeError("Parametr musi byt integer")

    # Vypocet koeficient determinantu
    detA = round(a1*(b2*c3 - b3*c2) - b1*(a2*c3 - a3*c2) + c1*(a2*b3 - a3*b2))

    if detA == 0:
        raise TypeError('Determinant se nesmi rovnat nule')
        return None

    # Spocitani determinantu matic
    detX1 = d1*(b2*c3 - b3*c2) - b1*(d2*c3 - d3*c2) + c1*(d2*b3 - d3*b2)
    detX2 = a1*(d2*c3 - d3*c2) - d1*(a2*c3 - a3*c2) + c1*(a2*d3 - a3*d2)
    detX3 = a1*(b2*d3 - b3*d2) - b1*(a2*d3 - a3*d2) + d1*(a2*b3 - a3*b2)

    # Pouziti Cramerova pravidla pro výpočet promnenych hodnot
    x = round(detX1 / detA)
    y = round(detX2 / detA)
    z = round(detX3 / detA)

    print("x je:", x)
    print("y je:", y)
    print("z je:", z)

    # Vraceni hodnot x,y,z
    return x, y, z


cramer_rule(2, 4, 3, 9, 5, 8, 7, 8, 9, 8, 2, 9)
