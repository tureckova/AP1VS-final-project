from prvocislo import primeNumber
from prvocislo import odpoved
import pytest

def test_primeNumber():
    """test x values"""
    assert primeNumber(1) == "Not valid input, please enter natural number"
    assert primeNumber(2) == "Prime number"
    assert primeNumber(-10) == "Not valid input, please enter natural number"
    
    with pytest.raises(TypeError):
        primeNumber(True)
        primeNumber("5")
    with pytest.raises(ValueError):
        primeNumber(2.0)       
        primeNumber(-2.1)
        primeNumber(2,5)
        primeNumber(5-2)

def test_odpoved():
    """test answer values values"""
    assert primeNumber("y" or "Y") == "Enter a number: "
    assert primeNumber("n" or "N") == "End of application"
    assert primeNumber("X") == "Choose y or n"
    