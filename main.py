"""
Uvod.

Závěrečný projekt předmětu Ap1VS
.. include:: README.md
Autori: Libor Vyleta, Filip Hajduch
"""
import math


def vypocetstrany(bod1x, bod1y, bod2x, bod2y):
    """
    Vypocet strany.

    :param bod1x: Vstupní parametr bod1x.
    :param bod1y: Vstupní parametr bod1y.
    :param bod2x: Vstupní parametr bod2x.
    :param bod2y: Vstupní parametr bod2y.
    :return: Vrací stranu
    """
    if type(bod1x) not in [int, float] or type(bod2x) not in [int, float] or \
            type(bod1y) not in [int, float] or type(
            bod2y) not in [int, float]:
        raise TypeError()
    else:
        a = bod2x - bod1x
        b = bod2y - bod1y
        strana = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
        return strana


def sestavitelnost(strana_a, strana_b, strana_c):
    """
    Sestavitelnost.

    :param strana_a: Vstupní parametr strana_a.
    :param strana_b: Vstupní parametr strana_b.
    :param strana_c: Vstupní parametr strana_c.
    :return: Vrací hodnotu True || False
    """
    if type(strana_a) not in [int, float] or type(strana_b) \
            not in [int, float] or type(strana_c) not in [int, float]:
        raise TypeError()
    else:
        if strana_a+strana_b > strana_c or strana_a+strana_c > strana_b or \
                strana_b+strana_c > strana_a:
            return True
        else:
            return False


def obsah(strana_a, strana_b, strana_c):
    """
    Výpočet obsahu přes Heronův vzorec.

    s -- potřebné pro výpočet obsahu obecného trojúhelníka
    :param strana_a: Vstupní parametr strana_a.
    :param strana_b: Vstupní parametr strana_b.
    :param strana_c: Vstupní parametr strana_c.
    :return: Vrací hodnotu obsahu
    """
    if type(strana_a) not in [int, float] or type(strana_b) not in \
            [int, float] or type(strana_c) not in [int, float]:
        raise TypeError()
    else:
        s = (strana_a + strana_b + strana_c) / 2
        obsah_s = math.sqrt(s * (s - strana_a) *
                            (s - strana_b) * (s - strana_c))
        return obsah_s


def obvod(strana_a, strana_b, strana_c):
    """
    Výpočet obvodu.

    :param strana_a: Vstupní parametr strana_a.
    :param strana_b: Vstupní parametr strana_b.
    :param strana_c: Vstupní parametr strana_c.
    :return: Vrací hodnotu obvodu
    """
    if type(strana_a) not in [int, float] or type(strana_b) not in \
            [int, float] or type(strana_c) not in [int, float]:
        raise TypeError()

    else:
        obvod_o = round(strana_a + strana_b + strana_c, 2)
        return obvod_o


def uhel(uhel_u_strany, strana_protilehla1, strana_protilehla2):
    """
    Výpočet úhlů.

    :param uhel_u_strany: Vstupní parametr uhel_u_strany.
    :param strana_protilehla1:
    Vstupní parametr strana_protilehla1.
    :param strana_protilehla2:
    Vstupní parametr strana_protilehla2.
    :return: Vrací hodnotu finalního úhlu
    """
    if type(uhel_u_strany) not in [int, float] or type(strana_protilehla1) \
            not in [int, float] or type(
            strana_protilehla2) not in [int, float]:
        raise TypeError()

    else:
        uhel1 = (math.pow(strana_protilehla1, 2) +
                 math.pow(strana_protilehla2, 2)
                 - math.pow(uhel_u_strany, 2)) / \
                (2 * strana_protilehla1 * strana_protilehla2)
        uhel_final = round(math.degrees(math.acos(uhel1)), 2)
        return uhel_final


def pravouhlost(alfa, beta, gama):
    """
    Výpočet pravoúhlosti.

    :param alfa: Vstupní parametr alfa.
    :param beta: Vstupní parametr beta.
    :param gama: Vstupní parametr gama.
    :return:True || False
    """
    if type(alfa) not in [int, float] or type(beta) not in [int, float] or \
            type(gama) not in [int, float]:
        raise TypeError()

    else:
        if alfa == 90 or beta == 90 or gama == 90:
            return True
        else:
            return False


def triangle(x1, y1, x2, y2, x3, y3):
    """Výpočet Trojúhelníku."""
    strana_a = vypocetstrany(x1, y1, x2, y2)
    strana_b = vypocetstrany(x2, y2, x3, y3)
    strana_c = vypocetstrany(x1, y1, x3, y3)

    if sestavitelnost(strana_a, strana_b, strana_c):
        obsah_s = obsah(strana_a, strana_b, strana_c)
        obvod_o = obvod(strana_a, strana_b, strana_c)
        uhel_alfa = uhel(strana_a, strana_b, strana_c)
        uhel_beta = uhel(strana_b, strana_a, strana_c)
        uhel_gama = uhel(strana_c, strana_b, strana_a)

        if pravouhlost(uhel_alfa, uhel_beta, uhel_gama):
            print("Trojuhelnik je pravouhly")
        else:
            print("Trojuhelnik neni pravouhly")

        print(strana_a)
        print(strana_b)
        print(strana_c)
        print(obsah_s)
        print(obvod_o)
        print(uhel_alfa)
        print(uhel_beta)
        print(uhel_beta)

    else:
        print("Trojuhelnik nelze sestavit")


triangle(0, 0, 6, 0, 3, 3)
