"""Importovani knihovny unittest."""
from RomanNumbers1 import intToRoman
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
        assert intToRoman(500) == 'D'

    def test14(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(900) == 'CM'

    def test15(self):
        """Kontrola správné hodnoty."""
        assert intToRoman(1000) == 'M'
