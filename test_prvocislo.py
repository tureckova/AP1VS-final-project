from prvocislo import primeNumber
import pytest


def test_primeNumber():
    """test x values"""
    assert primeNumber(-15) == "Not valid input, please enter natural number"
    # assert primeNumber(5) == "Prime number"
    assert primeNumber(-10) == "Not valid input, please enter natural number"

    with pytest.raises(TypeError):
        primeNumber("5")
    
    with pytest.raises(ValueError):
        primeNumber(True)
        primeNumber(2.0)
        primeNumber(-2.1)
        primeNumber(2, 5)
        primeNumber(5-2)
