from RomeNumbersMaybe import intToRoman
import pytest

def intToRomanTest():
    # test for numbers
    assert intToRomanTest(1256) == "MCCLVI"
    assert intToRomanTest(3521) == "MMMDXXI"
    assert intToRomanTest(379) == "CCCLXXIX"
    assert intToRomanTest(899) == "DCCCXCIX"

    # test for TypeError
    with pytest.raises(TypeError):
            intToRomanTest("Musi byt cislo!!!")
