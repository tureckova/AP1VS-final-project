"""Unit test for module IsPrime."""
from IsPrime import TestPrvociselnosti
from IsPrime import GetWholeNumber
import pytest
import sys
from unittest.mock import patch


def test_TestPrvociselnosti():
    """Test TestPrvociselnosti."""
    """r>=0 """
    assert TestPrvociselnosti(7) == "Jedná se o prvočíslo."
    """ r<0 """
    assert TestPrvociselnosti(0) == "Nejedná se o prvočíslo."
    assert TestPrvociselnosti(-7) == "Nejedná se o prvočíslo."
    assert TestPrvociselnosti(-1) == "Nejedná se o prvočíslo."

    """ return TypeError in other cases """
    with pytest.raises(TypeError):
        TestPrvociselnosti(True)
    with pytest.raises(TypeError):
        TestPrvociselnosti(5 + 5j)
    with pytest.raises(TypeError):
        TestPrvociselnosti("r")
    with pytest.raises(TypeError):
        TestPrvociselnosti(1.5)


def test_GetWholeNumber():
    """Test GetWholeNumber."""
    """Test where a valid number is passed as a command-line argument. """
    sys.argv[1] = '5'
    assert GetWholeNumber() == 5
    sys.argv[1] = ''
    """
    Test when no number is passed as a command-line argument.
    Then the user then enters a valid number.
    """
    with patch('builtins.input', return_value='7'):
        assert GetWholeNumber() == 7

    """
    Test when no number is passed as a command-line argument.
    Then the user then enters a text then valid number.
    """
    with patch('builtins.input', side_effect=['foo', 'bar', '7']):
        assert GetWholeNumber() == 7

    """
    Test when non integer is passed as a command-line argument.
    Then the user then enters a valid number.
    """
    sys.argv[1] = 'f'
    with patch('builtins.input', return_value='7'):
        assert GetWholeNumber() == 7
    sys.argv[1] = ''
