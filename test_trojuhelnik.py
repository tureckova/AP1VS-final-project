"""
Závěrečný projekt z předmětu AP1VS.

Skupina: ST1416
Projekt: Trojúhelník
Autoři: Martin Žůrek, David Fiala, David Tomeček, Josef Kužel, David Žídek

Kod sloužící k provedení unit testů
"""
from trojuhelnik import delkaStrany
from trojuhelnik import obvod
from trojuhelnik import obsah
from trojuhelnik import sestrojitelnost
from trojuhelnik import pravouhlost
import pytest


def test_delkaStrany():
    """Test na výpočet délky strany trojúhelníku ABC."""
    assert delkaStrany(2, 2, 9, 2) == 7

    """Zobrazí uživateli na konzoli hlášku TypeError"""
    with pytest.raises(TypeError):
        delkaStrany(9 + 10j, 5 + 1j, 5 + 4j, 10 + 8j)
        delkaStrany("v", "p", "r", "g")


def test_obvod():
    """Test na výpočet obvodu trojúhelníku ABC."""
    assert obvod(7, 5, 4) == 16

    """Zobrazí uživateli na konzoli hlášku TypeError"""
    with pytest.raises(TypeError):
        obvod(2 + 6j, 1 + 4j, 1 + 6j)
        obvod("o", "g", "a")


def test_obsah():
    """Test na výpočet obsahu trojúhelníku ABC."""
    assert obsah(8, 3, 6) == 7.644442425710328

    """Zobrazí uživateli na konzoli hlášku TypeError"""
    with pytest.raises(TypeError):
        obsah(1 + 6j, 3 + 9j, 3 + 7j)
        obsah("m", "r", "k")


def test_sestrojitelnost():
    """Test na ověření sestrojitelnosti trojúhelníku ABC."""
    assert sestrojitelnost(6, 8, 9) is True
    assert sestrojitelnost(2, 2, 4) is False

    """Zobrazí uživateli na konzoli hlášku TypeError"""
    with pytest.raises(TypeError):
        sestrojitelnost(9 + 6j, 8 + 2j, 6 + 7j)
        sestrojitelnost("t", "v", "c")


def test_pravouhlost():
    """Test na ověření pravoúhlosti  trojúhelníku ABC."""
    assert pravouhlost(10, 8, 6) is True
    assert pravouhlost(4, 6, 8) is False

    """Zobrazí uživateli na konzoli hlášku TypeError"""
    with pytest.raises(TypeError):
        pravouhlost(7 + 1j, 9 + 7j, 10 + 4j)
        pravouhlost("s", "o", "j")
