"""Importovani knihovny unittest."""
import unittest


class TestMethods(unittest.TestCase):
    """Trida urcena k testovani cisel a k nim prirazenym hodnot."""

    def test1(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(1) == 'I'

    def test2(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(2) == 'II'

    def test3(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(3) == 'III'

    def test4(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(4) == 'IV'

    def test5(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(5) == 'V'

    def test6(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(9) == 'IX'

    def test7(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(10) == 'X'

    def test8(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(40) == 'XL'

    def test9(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(50) == 'L'

    def test10(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(90) == 'XC'

    def test11(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(100) == 'C'

    def test12(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(400) == 'CD'

    def test13(self):
        """Kontrola správné hodnoty."""
        assert prevod(500) == 'D'

    def test14(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(900) == 'CM'

    def test15(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(1000) == 'M'


"""Prevod na rimske cislo."""


# Funkce bude převádět číslo do Římské soustavy
def intToRoman(cislo):
    # Vytvoříme platnou Římskou soustavu podle pořadí 0-9
    #    0   1000  2000  3000
    m = ["", "M", "MM", "MMM"]
    #    0   100  200   300    400   500  600   700     800    900
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    # Tento postup upraví číslo tak, abychom mohli dostat Římské číslo
    tisice = m[cislo // 1000]  # 2022 // 1000 -> "MM"
    sta = c[(cislo % 1000) // 100]  # 22 % 1000 = 22 // 100 -> ""
    desitky = x[(cislo % 100) // 10]  # 22 % 100 = 22 // 10 -> "XX"
    jednicky = i[cislo % 10]  # 2 % 10 = 2 -> "II"

    # Výsledek udá v pořadí tisíců/stovek/desítek/jedniček
    vysledek = (tisice + sta + desitky + jednicky)
    # Vracíme funkci kvůli testovacímu kódu
    return vysledek


# Tato funkce main je testovacím kódem
def main():
    unittest.main(exit=False)
    print("Zadej cislo, ktere chces prevest do Rimske soustavy: ")
    # Vstupní kód uživatele
    cislo = int(input())

    if cislo <= 0:
        print("Cislo mesmi byt nula nebo zaporne cislo")
    elif cislo >= 4000:
        print("Cislo nemuze byt vyssi nez 4000")
    else:
        print("Zadana hodnota neni cislo")
    # Výstupní číslo v Římské číselné soustavě
    print(intToRoman(cislo))


if __name__ == "__main__":
    main()