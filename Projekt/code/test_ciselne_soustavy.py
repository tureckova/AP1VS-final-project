"""Module to test functionality of the main file."""

from ciselne_soustavy import to_digits, to_decimal
from ciselne_soustavy import to_destination_base, convert


def test_to_digits():
    """Test the to_digits function."""
    assert to_digits(5) == [5]
    assert to_digits(12) == [1, 2]
    assert to_digits(390) == [3, 9, 0]
    assert to_digits(6541) == [6, 5, 4, 1]
    assert to_digits(515625) == [5, 1, 5, 6, 2, 5]
    assert to_digits(17263527183414) == [
        1, 7, 2, 6, 3, 5, 2, 7, 1, 8, 3, 4, 1, 4]


def test_to_decimal():
    """Test the to_decimal function."""
    assert to_decimal(2, 10, []) == 2
    assert to_decimal(16, 20, []) == 32
    assert to_decimal(8, 47, []) == 39
    assert to_decimal(2, 111100, []) == 60
    assert to_decimal(14, 154, []) == 270
    assert to_decimal(20, 134, []) == 464
    assert to_decimal(17, 1198, []) == 5363


def test_to_destination_base():
    """Test the to_destination_base function."""
    assert to_destination_base(2, 12) == ["1", "1", "0", "0"]
    assert to_destination_base(16, 58) == ["3", "A"]
    assert to_destination_base(8, 5830) == ["1", "3", "3", "0", "6"]
    assert to_destination_base(2, 78) == ["1", "0", "0", "1", "1", "1", "0"]
    assert to_destination_base(8, 78) == ["1", "1", "6"]
    assert to_destination_base(16, 78) == ["4", "E"]


def test_convert():
    """Test the convert function."""
    assert convert(10, 1, "6") == "111111"
    assert convert(2, 16, "11011") == "1B"
    assert convert(8, 10, "65") == "53"
    assert convert(10, 36, "1000") == "RS"
    assert convert(10, 16, "7899") == "1EDB"
    assert convert(16, 2, "69CB") == "110100111001011"
