from RomeNumbers import intToRoman
import pytest

def intToRomanTest():
    # test for numbers
    assert intToRoman(1256) == "MCCLVI"
    assert intToRoman(3521) == "MMMDXXI"
    assert intToRoman(379) == "CCCLXXIX"
    assert intToRoman(899) == "DCCCXCIX"
    
    # test for TypeError

    with pytest.raises(ValueError):
            intToRoman("Musi byt cislo!!!")