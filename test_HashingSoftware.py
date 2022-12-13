from HashingSoftware import HashPassw, CheckInput, CheckLength
import pytest

def test_HashPassw():
    assert HashPassw(1, "TezkeHeslo123", "SuperKratkyHash") == '7e803bead7cfded9b43e1e5a9cfbf0fc'
    assert HashPassw(2, "TezkeHeslo123", "SuperKratkyHash") == '32af788bf1f2d1b7c4fb039c5b3f81ae8081b63bdc426f53a149bd66fc0f9776d4b23b3f961c954140331b58ed8bf56e'
    assert HashPassw(3, "TezkeHeslo123", "SuperKratkyHash") == 'de6d9d4c3726426b07eefe687a8ad0e9df4e42e979a40504c0e9350b698b6656364ecaf01e2ce3f5b55e79224d3eee575f9bf8c50bd113d33badc3643d776d68'
    
    
def test_CheckInput():
    with pytest.raises(TypeError):
        CheckInput("string")

def test_CheckLength():
    with pytest.raises(ValueError):
        CheckLength("asdf", "asdfasdf")
        CheckLength("asdfasdfsadf", "ASDFASDFASFD")
