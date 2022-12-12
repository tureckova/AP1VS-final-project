from example import coding
from example import decoding
import pytest


def test_coding():
    assert coding('HELLO') == '.... . .-.. .-.. ---'
    assert coding('WORLD') == '.-- --- .-. .-.. -..'
    

def test_decoding():
    assert decoding('.... . .-.. .-.. ---') == 'HELLO'
    assert decoding('.-- --- .-. .-.. -..') == 'WORLD'

    
if __name__ == "__main__":
    pytest.main()
