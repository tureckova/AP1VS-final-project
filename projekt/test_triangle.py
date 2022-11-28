import pytest
from triangle import triangle

def test_triangle():
    # return relu
    assert triangle(1) == 1
    assert triangle(-5) == 0
    assert triangle(2.2) == 2.2
    assert triangle(-2.2) == 0

    # give typeError
    with pytest.raises(TypeError):
        triangle(1+5j)
        triangle(True)
        triangle("s")
