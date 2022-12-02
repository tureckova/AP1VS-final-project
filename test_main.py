import pytest
from main import triangle

def test_triangle():
    # return relu
    assert triangle(1, 2, 3, 4, 5, 6) == 1

    # give typeError
    with pytest.raises(TypeError):
        triangle(1+5j)
        triangle(True)
        triangle("s")

