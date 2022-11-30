from prvocislo import primeNumber
import pytest

def test_primeNumber():
    """test x values"""
    assert primeNumber(1) == "Prime number"
    assert primeNumber(2.0) == "Prime number"
    assert primeNumber(-10) == "Not a prime number"
    
    with pytest.raises(TypeError):
        primeNumber(True)
        primeNumber("5")