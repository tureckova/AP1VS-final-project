"""TerminalHasher Test File.

A command-line utility for viewing cryptographic
translations of user defined passwords.
"""


from main import intro, type_password, encrypt_password, get_input, choose_algorithm
"""Main file's functions."""


def test_intro(capsys):
    """test_intro tests the intro method."""
    intro()
    capture = capsys.readouterr()
    assert "Welcome to the best password hasher 2022" in capture.out


def test_get_input():
    """test_get_input tests the type_password method."""
    pass1 = get_input("testInput")
    pass2 = "testInput"
    assert pass2 == pass1


def test_encrypt_password():
    """test_encrypt_password tests the encrypt_password method."""
    assert "275ce9b199a2cbc9587bc281ad3f9e1313a65805" in encrypt_password(get_input("heslo@123"), choose_algorithm("1"), True)
    assert "b1c484b75a66c70fafd58e0a20c25cc005d85e60ff82a3a13a64e23847ff1340" in encrypt_password(get_input("Pudl42069"), choose_algorithm("2"), True)
    assert "19437359820bc1c7dea5000a2ccde2b0cbd29155b7e4fca650d8acafb3215683bbdf80f0d46268a7e347256e24c710e8beaa8cd4e2958b374d33d2ceda8d6212" in encrypt_password(get_input("vodaJeMokra."), choose_algorithm("3"), True)
    assert "4a9de83d3698498e4d29d9a31dcbdebc" in encrypt_password(get_input("imagineProlomenyAlgoritmus@&$~^ˇ~1234ASFN"), choose_algorithm("4"), True)


def test_type_password():
    """test_type_password tests the type_password method."""
    pass1 = type_password("testPassword&21")
    pass2 = "testPassword&21"
    assert pass2 == pass1


def test_choose_algorithm():
    algo1 = choose_algorithm("1")
    algo2 = choose_algorithm("2")
    algo3 = choose_algorithm("3")
    algo4 = choose_algorithm("4")
    algo5 = choose_algorithm("5")
    algo6 = choose_algorithm("asd")
    assert algo1 == "sha1"
    assert algo2 == "sha256"
    assert algo3 == "sha512"
    assert algo4 == "md5"
    assert algo5 == ""
    assert algo6 == ""
