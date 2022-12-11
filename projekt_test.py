from projekt import speak, generateJoke, main
import pytest

def test_speak():
    # TypeError if needed
    with pytest.raises(TypeError):
        speak(True)
        speak(int)

def test_generateJoke():
    # TypeError if needed
    with pytest.raises(TypeError):
        generateJoke(True)
    # test for userInput
    assert type(generateJoke(1)) == str
    # test if word "Chuck" is in GenerateJoke(2)
    word = "Chuck"
    assert word in generateJoke(2)
    
def test_main():
    # TypeError if needed
    with pytest.raises(TypeError):
        main(int)
