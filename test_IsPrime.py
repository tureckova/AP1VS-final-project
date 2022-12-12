"""Unit test for module IsPrime."""
from IsPrime import TestPrvociselnosti
import pytest


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
