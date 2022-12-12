from example import coding
from example import decoding
import pytest


def test_coding_edge_cases():
    assert coding('HELLO') == '.... . .-.. .-.. --- '
    assert coding('123') == '1 2 3 ''
    assert coding(' ') == KeyError
    assert coding(',') == KeyError  
test_coding_edge_cases()

#To write unit tests for the decoding() function, we can test that it decodes strings correctly by comparing the output of the function with the expected result. For example:



def test_decoding_edge_cases():
    assert decoding('.... . .-.. .-.. ---') == 'HELLO'
    assert decoding('.-- .-. .. -. ..-. ') == 'WORLD'
    assert decoding('1 2 3 ') == '123'
    assert decoding(' ') == KeyError

test_decoding_edge_cases()
