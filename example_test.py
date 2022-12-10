from example import coding
from example import decoding
from example import selection
import pytest

def test_coding():
    #test coding for letters A-Z
    assert test_coding('A') == '.-'
    assert test_coding('B') == '-...'
    assert test_coding('C') == '-.-.'
    assert test_coding('D') == '-..'
    assert test_coding('E') == '.'
    assert test_coding('F') == '..-.' 
    assert test_coding('G') == '--.'
    assert test_coding('H') == '....'
    assert test_coding('I') == '..'
    assert test_coding('J') == '.---'
    assert test_coding('K') == '-.-'
    assert test_coding('L') == '.-..'
    assert test_coding('M') == '--'
    assert test_coding('N') == '-.'
    assert test_coding('O') == '---'
    assert test_coding('P') == '.--.'
    assert test_coding('Q') == '--.-'
    assert test_coding('R') == '.-.'
    assert test_coding('S') == '...'
    assert test_coding('T') == '-'
    assert test_coding('U') == '..-'
    assert test_coding('V') == '...-'
    assert test_coding('W') == '.--'
    assert test_coding('X') == '-..-'
    assert test_coding('Y') == '-.--'
    assert test_coding('Z') == '--..'

    # test typeerror
    with pytest.raises(TypeError):
        test_coding(4)
        test_coding(True)
        test_coding("r")
        
def test_selection():

def test_decoding() :
    #test decoding for letters A-Z
    assert test_decoding('.-') == 'A'
    assert test_decoding('-...') == 'B'
    assert test_decoding('-.-.') == 'C'
    assert test_decoding('-..') == 'D'
    assert test_decoding('.') == 'E'
    assert test_decoding('..-.') == 'F'
    assert test_decoding('--.') == 'G'
    assert test_decoding('....') == 'H'
    assert test_decoding('..') == 'I'
    assert test_decoding('---') == 'J'
    assert test_decoding('-.-') == 'K'
    assert test_decoding('.-..') == 'L'
    assert test_decoding('--') == 'M'
    assert test_decoding('-.') == 'N'
    assert test_decoding('---') == 'O'
    assert test_decoding('.--.') == 'P'
    assert test_decoding('--.-') == 'Q'
    assert test_decoding('.-.') == 'R'
    assert test_decoding('...') == 'S'
    assert test_decoding('-') == 'T'
    assert test_decoding('..-') == 'U'
    assert test_decoding('...-') == 'V'
    assert test_decoding('.--') == 'W'
    assert test_decoding('-..-') == 'X'
    assert test_decoding('-.--') == 'Y'
    assert test_decoding('--..') == 'Z'
