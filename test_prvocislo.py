"""Test module."""
from prvocislo import primeNumber, odpoved
import pytest


def test_primeNumber():
    """Test x values."""
    assert primeNumber(2)
    assert not primeNumber(6)
    assert not primeNumber(22)
    assert primeNumber(73)


def test_odpoved():
    """Test odpoved function."""
    assert odpoved(2) == "Prime number"
    assert odpoved(6) == "Not a prime number"

    with pytest.raises(ValueError):
        odpoved("j")

    with pytest.raises(TypeError):
        odpoved(-5)
        odpoved(1)
