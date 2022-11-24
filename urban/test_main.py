"""
Unit test for main.py
"""

from main import *
import pytest


def test_intro(capsys):
    Intro()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Welcome to the best password hasher 2022"

def test_choose_algorithm():
    out1 = TypePassword()
    out2 = TypePassword()
    assert out1 == out2
def test_type_password():
    text1 = TypePassword()
    text2 = TypePassword()
    assert text1 == text2

def test_encrypt_password(password, type):
    #case md5
    EncryptPassword(password,type)
    #case sha1
    EncryptPassword(password, type)
    #case sha256
    EncryptPassword(password, type)
    #case sha512
    EncryptPassword(password, type)
def test_get_input(capsys):
    text1 = print("bagr")
    text2 = captured = capsys.readouterr()
    assert get_input(text1) == text2