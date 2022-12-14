from trojuholnik_v2 import obvod_Stran, Obsah_Trojuholnika, strana, uhol

"""Vytvorenie funkcie pre testovanie obvodu."""


def test_obvodu():
    """Porovnanie obvodu,ci sa vysledok zhoduje so zadanou hodnotou."""
    assert obvod_Stran(2, 2, 2) == 6.0


"""Vytvorenie funkcie pre testovanie obsahu"""


def test_Obsah():
    """Porovnanie obsahu, že ci sa vysledok zhoduje so zadanou hodnotou."""
    assert Obsah_Trojuholnika(5, 5, 8) == 12.0


"""Vytvorenie funkcie pre testovanie Strany"""


def test_Strana():
    """Porovnani nadefinovanu funkciu na vypocet strany a overenie vysledku."""
    assert strana(1, 2, 2, 1) == (((1 - 2) ** 2 + (2 - 1) ** 2) ** (1 / 2))


"""Vytvorenie funkcie pre testovanie Uhlu"""


def test_Uhol():
    """Porovnani nadefinovane funkce na vypocet uhlu a overeni vysledku."""
    assert uhol(0, 1, 1, 0, 0, 0) == 90.00000000000001
