"""
PyTest.

Závěrečný projekt předmětu Ap1VS
Autori: Libor Vyleta, Filip Hajduch
"""
import pytest
from main import vypocetstrany
from main import sestavitelnost
from main import obsah
from main import obvod
from main import uhel
from main import pravouhlost


def test_vypocetstrany():
    """Test výpočet strany."""
    assert vypocetstrany(0, 0, 1, 1) == 1.4142135623730951

    """Give typeError."""
    with pytest.raises(TypeError):
        vypocetstrany(1 + 5j, 1 + 5j, 1 + 5j, 1 + 5j)
        vypocetstrany("a", "b", "c", "d")


def test_sestavitelnost():
    """Test sestavitelnost."""
    assert sestavitelnost(4, 5, 6) is True
    assert sestavitelnost(0, 0, 0) is False

    """Give typeError."""
    with pytest.raises(TypeError):
        sestavitelnost(1 + 5j, 1 + 5j, 1 + 5j)
        sestavitelnost("a", "b", "c")


def test_obsah():
    """Test obsah."""
    assert obsah(4, 5, 6) == 9.921567416492215

    """Give typeError."""
    with pytest.raises(TypeError):
        obsah(1 + 5j, 1 + 5j, 1 + 5j)
        obsah("a", "b", "c")


def test_obvod():
    """Test obvod."""
    assert obvod(1, 1, 1) == 3

    """Give typeError."""
    with pytest.raises(TypeError):
        obvod(1 + 5j, 1 + 5j, 1 + 5j)
        obvod("a", "b", "c")


def test_uhel():
    """Test úhel."""
    assert uhel(4, 5, 6) == 41.41

    # give typeError
    with pytest.raises(TypeError):
        uhel(1 + 5j, 1 + 5j, 1 + 5j)
        uhel("a", "b", "c")


def test_pravouhlost():
    """Pravoúhlost."""
    assert pravouhlost(90, 45, 45) is True
    assert pravouhlost(45, 90, 45) is True
    assert pravouhlost(45, 45, 90) is True
    assert pravouhlost(60, 60, 60) is False

    # give typeError
    with pytest.raises(TypeError):
        pravouhlost(1 + 5j, 1 + 5j, 1 + 5j)
        pravouhlost("a", "b", "c")
