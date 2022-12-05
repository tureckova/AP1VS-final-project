from functools import partialmethod
from prvocislo import primeNumber, odpoved
import pytest


def test_primeNumber():
    """test x values"""
    assert primeNumber(2) == True
    assert primeNumber(6) == False
    assert primeNumber(22) == False
    assert primeNumber(73) == True


def test_odpoved():
    assert odpoved is None
        
