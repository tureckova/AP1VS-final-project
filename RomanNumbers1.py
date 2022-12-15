"""Funkce bude převádět číslo do Římské soustavy."""


def intToRoman(cislo):
    """Vytvoříme platnou Římskou soustavu podle pořadí 0-9.
:param cislo: vstupni promena funkce cislo !=<0 cislo!>4000
:return: vraci vysledek po prevodu promenne cislo na rimskou soustavu
"""
    if type(cislo) not in [int]:
        raise TypeError("Zadana hodnota neni cislo")
    if int(cislo) <= 0:
        raise ValueError("Cislo mesmi byt nula nebo zaporne cislo")
    if int(cislo) >= 4000:
        raise ValueError("Cislo nemuze byt vyssi nez 4000")
    
    """ 0   1000  2000  3000."""
    m = ["", "M", "MM", "MMM"]
    """    0   100  200   300    400   500  600   700     800    900."""
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    """Tento postup upraví číslo tak, abychom mohli dostat Římské číslo."""
    tisice = m[cislo // 1000]
    """ 2022 // 1000 -> "MM" """
    sta = c[(cislo % 1000) // 100]
    """ 22 % 1000 = 22 // 100 -> "" """
    desitky = x[(cislo % 100) // 10]
    """ 22 % 100 = 22 // 10 -> "XX" """
    jednicky = i[cislo % 10]
    """ 2 % 10 = 2 -> "II" """
    
    """ Výsledek udá v pořadí tisíců/stovek/desítek/jedniček."""
    vysledek = (tisice + sta + desitky + jednicky)

    """ Vracíme funkci kvůli testovacímu kódu."""
    return vysledek


def main():
    """Tato funkce main je testovacím kódem."""
    print("Zadej cislo, ktere chces prevest do Rimske soustavy: ")
    """ Vstupní kód uživatele. """
    cislo = int(input())

    """Výstupní číslo v Římské číselné soustavě."""
    print(intToRoman(cislo))


if __name__ == "__main__":
    main()
