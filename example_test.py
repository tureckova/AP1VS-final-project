"""Unit test."""
from example import coding
from example import decoding
import pytest


def test_decoding():
    """Test decoding."""
    assert decoding('...././.-../.-../---') == ('HELLO')
    assert decoding('-.../') == ('B ')


def test_coding():
    """Test coding."""
    assert type(coding('HELLO')) == str
    assert coding('MAM RAD JABLKA') == (
        ' --/.-/--//.-./.-/-..//.---/.-/-.../.-../-.-/.-/')
    assert coding('B') == ' -.../'


if __name__ == "__main__":
    pytest.main()
