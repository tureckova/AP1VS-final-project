"""
Závěrečný projekt z předmětu AP1VS.

Skupina: ST1416
Projekt: Trojúhelník
Autoři: Martin Žůrek, David Fiala, David Tomeček, Josef Kužel, David Žídek

Hlavní kód projektu trojúhelník
"""
import math  # slouží k pozdějšímu použití v počítání
import time  # slouží k uspání kódu


def delkaStrany(prvniBodX, prvniBodY, druhyBodX, druhyBodY):
    """
    Výpočet délky strany trojúhelníku ABC.

    :param prvniBodX: Vstupní parametr souřadnice x prvního bodu
    :param prvniBodY: Vstupní parametr souřadnice y prvního bodu
    :param druhyBodX: Vstupní parametr souřadnice x druhého bodu
    :param druhyBodY: Vstupní parametr souřadnice y druhého bodu
    :return: Vrací délku strany trojúhelníku ABC
    """
    if (type(prvniBodX) not in [int, float] or
            type(prvniBodY) not in [int, float] or
            type(druhyBodX) not in [int, float] or
            type(druhyBodY) not in [int, float]):
        raise TypeError()
    else:
        strana = math.sqrt(math.pow(prvniBodX - druhyBodX, 2) +
                           math.pow(prvniBodY - druhyBodY, 2))
        return strana


def obvod(stranaA, stranaB, stranaC):
    """
    Výpočet velikosti obvodu trojúhelníku ABC.

    :param stranaA: Vstupní parametr velikost strany a
    :param stranaB: Vstupní parametr velikost strany b
    :param stranaC: Vstupní parametr velikost strany c
    :return: Vrací velikost obvodu trojúhelníku ABC
    """
    if (type(stranaA) not in [int, float] or
            type(stranaB) not in [int, float] or
            type(stranaC) not in [int, float]):
        raise TypeError()
    else:
        obvod = stranaA + stranaB + stranaC
        return obvod


def obsah(stranaA, stranaB, stranaC):
    """
    Výpočet velikosti obsahu trojúhelníku ABC.

    :param stranaA: Vstupní parametr velikost strany a
    :param stranaB: Vstupní parametr velikost strany b
    :param stranaC: Vstupní parametr velikost strany c
    s - pomocná proměnná pro výpočet obsahu trojúhelníku
    :return: Vrací velikost obsahu trojúhelníku ABC
    """
    if (type(stranaA) not in [int, float] or
            type(stranaB) not in [int, float] or
            type(stranaC) not in [int, float]):
        raise TypeError()
    else:
        s = (stranaA + stranaB + stranaC) / 2
        obsah = math.sqrt(s * (s - stranaA) * (s - stranaB) * (s - stranaC))
        return obsah


def sestrojitelnost(stranaA, stranaB, stranaC):
    """
    Ověření sestrojitelnosti trojúhelníku ABC.

    :param stranaA: Vstupní parametr velikost strany a
    :param stranaB: Vstupní parametr velikost strany b
    :param stranaC: Vstupní parametr velikost strany c
    :return: Vrací hodnotu ANO nebo NE
    """
    if (type(stranaA) not in [int, float] or
            type(stranaB) not in [int, float] or
            type(stranaC) not in [int, float]):
        raise TypeError()
    else:
        if ((stranaA + stranaB > stranaC) and
                (stranaB + stranaC > stranaA) and
                (stranaC + stranaA > stranaB)):
            return True
        else:
            return False


def pravouhlost(stranaA, stranaB, stranaC):
    """
    Ověření pravoúhlosti trojúhelníku.

    :param stranaA: Vstupní parametr velikost strany a
    :param stranaB: Vstupní parametr velikost strany b
    :param stranaC: Vstupní parametr velikost strany c
    :return: Vrací hodnotu ANO nebo NE
    """
    if (type(stranaA) not in [int, float] or
            type(stranaB) not in [int, float] or
            type(stranaC) not in [int, float]):
        raise TypeError()
    else:
        if ((math.pow(stranaA, 2) + math.pow(stranaB, 2) ==
             math.pow(stranaC, 2)) or
                (math.pow(stranaB, 2) + math.pow(stranaC, 2) ==
                 math.pow(stranaA, 2)) or
                (math.pow(stranaC, 2) + math.pow(stranaA, 2) ==
                 math.pow(stranaB, 2))):
            return True
        else:
            return False


def trojuhelnik(aX, aY, bX, bY, cX, cY):
    """Výpis vlastností trojúhelníku ABC."""
    stranaA = delkaStrany(bX, bY, cX, cY)  # vypočítá délku strany A
    stranaB = delkaStrany(aX, aY, cX, cY)  # vypočítá délku strany B
    stranaC = delkaStrany(aX, aY, bX, bY)  # vypočítá délku strany C
    vysledekObvod = obvod(stranaA, stranaB, stranaC)
    vysledekObsah = obsah(stranaA, stranaB, stranaC)

    if sestrojitelnost(stranaA, stranaB, stranaC):  # ověří sestrojitelnost
        print("Bod A = [%.1f, %.1f]" % (aX, aY))  # vypíše souřadnice bodu A
        print("Bod B = [%.1f, %.1f]" % (bX, bY))  # vypíše souřadnice bodu B
        print("Bod C = [%.1f, %.1f]" % (cX, cY))  # vypíše souřadnice bodu C
        time.sleep(2)  # uspí kód na 2s
        print()  # vypíše prázdný řádek
        print("Délka strany a = %.1f cm." % stranaA)  # vypíše délku strany a
        print("Délka strany b = %.1f cm." % stranaB)  # vypíše délku strany b
        print("Délka strany c = %.1f cm." % stranaC)  # vypíše délku strany c
        time.sleep(2)  # uspí kód na 2s
        print()  # vypíše prázdný řádek
        print("Trojúhelník ABC má obvod = %.1f cm." % vysledekObvod)
        time.sleep(2)  # uspí kód na 2s
        print()  # vypíše prázdný řádek
        print("Trojúhelník ABC má obsah = %.1f cm2." % vysledekObsah)
        time.sleep(2)  # uspí kód na 2s
        print()  # vypíše prázdný řádek
        if pravouhlost(stranaA, stranaB, stranaC):  # ověří pravoúhlost
            print("Trojúhelník ABC je pravoúhlý.")
        else:
            print("Trojúhelník ABC není pravoúhlý.")
        time.sleep(2)  # uspí kód na 2s
        print()  # vypíše prázdný řádek
        print("Trojúhelník ABC lze sestrojit.")
    else:
        print("Trojúhelník ABC nelze sestrojit.")


trojuhelnik(2, 5, 2, 2, 9, 2)  # předává hodnoty souřadnic pro trojuhelnik
