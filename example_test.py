"""Unit test."""
from example import coding
from example import decoding
import pytest


def test_decoding():
    """Test decoding."""
    assert decoding('...././.-../.-../---') == ('HELLO')


def test_coding():
    """Test coding."""
    assert coding('HELLO') == ('...././.-../.-../---')


if __name__ == "__main__":
    pytest.main()
