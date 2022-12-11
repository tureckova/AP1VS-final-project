from example import coding
from example import decoding
import pytest


def test_coding_edge_cases():
    assert coding('HELLO') == '.... . .-.. .-.. ---'
    assert coding('Hello,World') == KeyError
    assert coding('1') == KeyError
    assert coding('HELLO world') == '.... . .-.. .-.. ---  .-- --- .-. .-.. -..'
    
test_coding_edge_cases()





def test_decoding_edge_cases():
    assert decoding('.... . .-.. .-.. ---') == 'HELLO'
    assert decoding('.-- --- .-. .-.. -..') == 'WORLD'
    assert decoding('.... . .-.. .-.. ---  .-- --- .-. .-.. -..') == 'HELLO WORLD'
    assert decoding('.... . .-.. .-.. ---  -- .-. .. ... - / .-- .-. .. -. ..-.') == KeyError
    assert decoding('1 2 3 ') == KeyError
    

test_decoding_edge_cases()