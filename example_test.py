"""Coding."""
from example import coding
from example import decoding
import pytest


def test_decoding():
    """Coding."""
    assert decoding('.... . .-.. .-.. ---') == ('HELLO')


def test_coding():
    """Coding."""
    assert type(coding('HELLO')) == str


if __name__ == "__main__":
    pytest.main()
