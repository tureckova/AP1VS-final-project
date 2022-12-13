from cramersrule import determinant
import pytest

def test_determinant():
    """ Test cramerova pravidla."""


    assert determinant(2,1,3,1,-2,1,3,2,2) == 13
    assert determinant(1,2,4,3,1,3,2,3,2) == 21
    
    with pytest.raises(TypeError):
        determinant("nvm")
        determinant(True)

    
