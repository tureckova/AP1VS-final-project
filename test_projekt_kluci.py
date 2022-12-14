from projekt_kluci import retezec
import pytest

def test_retezec():
    # retezec == str
    assert retezec("slovo")== (5, 'o', 's', 1.25, {'o': 2, 's': 1, 'l': 1, 'v': 1})
    # returt TypeError in other cases
    with pytest.raises(TypeError):
        retezec(False)
    with pytest.raises(TypeError):
        retezec(1)
