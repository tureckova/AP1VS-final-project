"""Unit test."""
from cramerovo_pravidlo import cramer_rule
import pytest


def test_cramer_rule():
    """Test cramerova pravidla."""
    assert cramer_rule(2, 4, 3, 9, 5, 8, 7, 8, 9, 1, 4, 5) == (7, 11, -17)
    assert cramer_rule(5, 7, 3, 9, 3, 8, 7, 8, 9, 2, 4, 9) == (1, 1, 0)
    assert cramer_rule(2, 4, 3, 9, 5, 8, 7, 8, 9, 8, 2, 9) == (-5, 8, -5)
    assert cramer_rule(1, 2, 5, 7, 12, 9, 6, 5, 15, 10, 11, 14) == (0, -1, 2)
    assert cramer_rule(3, 4, 5, 12, 9, 3, 4, 15, 8, 2, 6, 21) == (1, -1, 3)
    assert cramer_rule(1, 3, 3, 3, 3, 8, 7, 8, 9, 2, 4, 9) == (1, 0, 0)

    with pytest.raises(TypeError):
        cramer_rule("s", "a", "l", "A", "s", "a", "S", "x", "s", "v", "q", "a")
