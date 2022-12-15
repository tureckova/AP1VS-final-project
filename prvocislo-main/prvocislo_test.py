"""Test module prvocislo."""
from prvocislo import *
import pytest

def test_type_prime():
  """Test function type_prime"""
  assert counting_prime(1) == False
  assert counting_prime(5) == True
  assert counting_prime("3") == True
  assert counting_prime("6") == False
  assert counting_prime("11.0") == False


def test_counting_prime():
  """Test function counting_prime"""
  # test case r=0
  assert counting_prime(1) == False 
  assert counting_prime(2) == True
  assert counting_prime(3) == True
  assert counting_prime(23) == True
  # test case r<=0
  assert counting_prime(0) == False
  assert counting_prime(-1) == False
  assert counting_prime(-2) == False
  assert counting_prime(-5) == False
  assert counting_prime(-9) == False


def test_power():
  """Test function power"""
  assert power(2,12) != 1
  assert power(2,13) == 1
  assert power(5,31) != 1


def test_is_prime():
  """Test function is_prime"""
  assert is_prime(2,3) == True
  assert is_prime(6,3) == False
  assert is_prime(17,3) == True
