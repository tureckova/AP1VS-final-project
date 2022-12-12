"""
Závěrečný projekt z předmětu AP1VS.
Skupina: ST1416
Projekt: Trojúhelník
Autoři: Martin Žůrek, David Fiala, David Tomeček, Josef Kužel, David Žídek
.. include:: README.md
"""
import math
import time


def delkaStrany(bodXx, bodXy, bodYx, bodYy):
    """
    Výpočet délky strany trojúhelníku ABC.
    :param bodXx: Vstupní parametr souřadnice x bodu X
    :param bodXy: Vstupní parametr souřadnice y bodu X
    :param bodYx: Vstupní parametr souřadnice x bodu Y
    :param bodYy: Vstupní parametr souřadnice y bodu Y
    :return: Vrací délku strany trojúhelníku ABC
    """
    if type(bodXx) not in [int, float] or type(bodXy) not in [int, float] or type(bodYx) not in [int, float] or type(bodYy) not in [int, float]:
        raise TypeError()
    else:
        strana = math.sqrt(math.pow(bodYx - bodXx, 2) + math.pow(bodYx - bodXx, 2))
        return strana


def obvod(stranaA, stranaB, stranaC):
    """
    Výpočet velikosti obvodu trojúhelníku ABC.
    :param stranaA: Vstupní parametr velikost strany a
    :param stranaB: Vstupní parametr velikost strany b
    :param stranaC: Vstupní parametr velikost strany c
    :return: Vrací velikost obvodu trojúhelníku ABC
    """
    if type(stranaA) not in [int, float] or type(stranaB) not in [int, float] or type(stranaC) not in [int, float]:
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
    if type(stranaA) not in [int, float] or type(stranaB) not in [int, float] or type(stranaC) not in [int, float]:
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
    if type(stranaA) not in [int, float] or type(stranaB) not in [int, float] or type(stranaC) not in [int, float]:
        raise TypeError()
    else:
        if ((stranaA + stranaB > stranaC) or
            (stranaB + stranaC > stranaA) or
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
    if type(stranaA) not in [int, float] or type(stranaB) not in [int, float] or type(stranaC) not in [int, float]:
        raise TypeError()
    else:
        if ((math.pow(stranaA, 2) + math.pow(stranaB, 2) == math.pow(stranaC, 2)) or
            (math.pow(stranaB, 2) + math.pow(stranaC, 2) == math.pow(stranaA, 2)) or
            (math.pow(stranaC, 2) + math.pow(stranaA, 2) == math.pow(stranaB, 2))):
            return True
        else:
            return False


def trojuhelnik(aX, aY, bX, bY, cX, cY):
    """Výpis vlastností trojúhelníku ABC."""
    stranaA = delkaStrany(bX, bY, cX, cY)
    stranaB = delkaStrany(cX, cY, aX, aY)
    stranaC = delkaStrany(aX, aY, bX, bY)
    vysledekObvod = obvod(stranaA, stranaB, stranaC)
    vysledekObsah = obsah(stranaA, stranaB, stranaC)
    
    if sestrojitelnost(stranaA, stranaB, stranaC):
        print("Bod A = [%.1f, %.1f]" %(aX, aY))
        print("Bod B = [%.1f, %.1f]" %(bX, bY))
        print("Bod C = [%.1f, %.1f]" %(cX, cY))
        time.sleep(2)
        print( )
        print("Délka strany a = %.1f cm." %stranaA)
        print("Délka strany b = %.1f cm." %stranaB)
        print("Délka strany c = %.1f cm." %stranaC)
        time.sleep(2)
        print( )
        print("Trojúhelník ABC má obvod = %.1f cm." %vysledekObvod)
        time.sleep(2)
        print( )
        print("Trojúhelník ABC má obsah = %.1f cm2." %vysledekObsah)
        time.sleep(2)
        print( )
        if pravouhlost(stranaA, stranaB, stranaC):
            print("Trojúhelník ABC je pravoúhlý.")
        else:
            print("Trojúhelník ABC není pravoúhlý.")
        time.sleep(2)
        print( )
        print("Trojúhelník ABC lze sestrojit.")
    else:
        print("Trojúhelník ABC nelze sestrojit.")
        
trojuhelnik(-3, 3, 1, -3, 3, -1)
