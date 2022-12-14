"""Import functions from projekt."""
from projekt import speak, generateJoke, main
import pytest


def test_speak():
    """Define test speak function."""
    # TypeError if needed
    with pytest.raises(TypeError):
        speak(True)
        speak(int)


def test_generateJoke():
    """Define test generateJoke function."""
    # TypeError if needed
    with pytest.raises(TypeError):
        generateJoke(True)
    # test for userInput
    assert type(generateJoke(1)) == str
    assert type(generateJoke(2)) == str
    assert type(generateJoke(3)) == str
    # test if word "Chuck" is in GenerateJoke(2)
    word = "Chuck"
    assert word in generateJoke(2)


def test_main():
    """Define test main function."""
    # TypeError if needed
    with pytest.raises(TypeError):
        main(int)
