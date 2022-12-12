from example import coding
from example import decoding
import pytest


def test_coding():
    assert coding('HELLO') == '.... . .-.. .-.. ---'
    assert coding('Hello,World') == KeyError
    assert coding('1') == KeyError
    assert coding('HELLO world') == '.... . .-.. .-.. ---  .-- --- .-. .-.. -..'
    

def test_decoding():
    assert decoding('.... . .-.. .-.. ---') == 'HELLO'
    assert decoding('.-- --- .-. .-.. -..') == 'WORLD'
    assert decoding('.... . .-.. .-.. ---  .-- --- .-. .-.. -..') == 'HELLO WORLD'
    assert decoding('.... . .-.. .-.. ---  -- .-. .. ... - / .-- .-. .. -. ..-.') == KeyError
    assert decoding('1 2 3 ') == KeyError
    
if __name__ == "__main__":
    pytest.main()
