from projekt import speak
import pytest

def test_speak():
    # TypeError if needed
    with pytest.raises(TypeError):
        speak(True)
        speak(int)
