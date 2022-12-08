"""TerminalHasher Test File.

A command-line utility for viewing cryptographic
translations of user defined passwords.
"""


from main import intro, type_password, encrypt_password, get_input
"""Main file's functions."""


def test_intro(capsys):
    """test_intro tests the intro method."""
    intro()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Welcome to the best password hasher 2022"


def test_choose_algorithm():
    """test_choose_algorithm tests the choose_algorithm method."""
    out1 = type_password()
    out2 = type_password()
    assert out1 == out2


def test_type_password():
    """test_type_password tests the type_password method."""
    text1 = type_password()
    text2 = type_password()
    assert text1 == text2


def test_encrypt_password(password, hash_type):
    """test_encrypt_password tests the encrypt_password method."""
    # case md5
    encrypt_password(password, hash_type)
    # case sha1
    encrypt_password(password, hash_type)
    # case sha256
    encrypt_password(password, hash_type)
    # case sha512
    encrypt_password(password, hash_type)


def test_get_input(capsys):
    """test_get_input tests the get_input method."""
    text1 = print("bagr")
    text2 = capsys.readouterr()
    assert get_input(text1) == text2
