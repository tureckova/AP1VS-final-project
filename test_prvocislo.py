from prvocislo import primeNumber
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
        primeNumber(2.55.55)        
        primeNumber(-2.1)
        primeNumber(2,5)