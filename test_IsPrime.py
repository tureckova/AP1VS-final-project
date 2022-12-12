"""Unit test for module circle"""
from IsPrime import TestPrvociselnosti
import pytest

def test_TestPrvociselnosti():
    # r>=0
    assert TestPrvociselnosti(7) == "Jedná se o prvočíslo."
    assert TestPrvociselnosti(1.5) == "Nejedná se o prvočíslo."
    # r<0
    assert TestPrvociselnosti(0) == "Nejedná se o prvočíslo."
    assert TestPrvociselnosti(-7) == "Nejedná se o prvočíslo."
    assert TestPrvociselnosti(-1) == "Nejedná se o prvočíslo."

    