from HashingSoftware import HashPassw, CheckInput, CheckLenght
import pytest

def test_HashPassw():
    # HashPassw for
    assert HashPassw(1, "TezkeHeslo123", "SuperKratkyHash") == '7e803bead7cfded9b43e1e5a9cfbf0fc'

def test_CheckInput():
    # CheckInput for
    assert CheckInput()
    assert CheckInput()
    assert CheckInput()

    #TypeError if needed
    with pytest.raises(TypeError):
        CheckInput("string")

    

def test_CheckLength():
    # TypeError if needed
    with pytest.raises(ValueError):
        CheckLenght("asdf", "asdfasdf)
        CheckLenght("asdfasdfsadf", "ASDFASDFASFD")
