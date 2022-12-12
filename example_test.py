from example import coding
from example import decoding
import pytest


def test_coding():
    assert test_coding('A') == '.-'
    assert test_coding('B') == '-...'
    

def test_decoding():
    assert test_decoding('.-') == 'A'
    assert test_decoding('-...') == 'B'

    
if __name__ == "__main__":
    pytest.main()