from example import coding
from example import decoding
import pytest


def test_decoding():
    assert decoding('.... . .-.. .-.. ---') == ('HELLO')
    

def test_coding():
    assert type(coding('HELLO')) == str


    
if __name__ == "__main__":
    pytest.main()