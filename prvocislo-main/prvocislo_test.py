"""Test module prvocislo."""
from prvocislo import type_prime, counting_prime, power, is_prime
import pytest


def test_type_prime():
    """Test function type_prime."""
    assert type_prime(1) is False
    assert type_prime(5) is True
    assert type_prime(11.0) is True
    assert type_prime(11.1) is False
    assert type_prime("3") is True
    assert type_prime("6") is False
    assert type_prime("11.0") is True
    assert type_prime("11.1") is False


def test_counting_prime():
    """Test function counting_prime."""
    # test case r=0
    assert counting_prime(1) is False
    assert counting_prime(2) is True
    assert counting_prime(3) is True
    assert counting_prime(23) is True
    # test case r<=0
    assert counting_prime(0) is False
    assert counting_prime(-1) is False
    assert counting_prime(-2) is False
    assert counting_prime(-5) is False
    assert counting_prime(-9) is False
    with pytest.raises(TypeError):
        counting_prime("5")
    with pytest.raises(TypeError):
        counting_prime([])


def test_power():
    """Test function power."""
    assert power(2, 12) != 1
    assert power(2, 13) == 1
    assert power(5, 35) != 1


def test_is_prime():
    """Test function is_prime."""
    assert is_prime(2, 3) is True
    assert is_prime(6, 3) is False
    assert is_prime(17, 3) is True
