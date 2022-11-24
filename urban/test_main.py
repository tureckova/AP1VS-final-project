"""
Unit test for main.py
"""
from main import *
import pytest

def test_intro(capsys):
    Intro()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Welcome to the best password hasher 2022"

"""
def test_choose_algorithm():

def test_type_password():

def test_encrypt_password():
"""