"""Testing module."""
from MorseCodeTranslator import continue_or_exit, copy_or_not, encrypt, \
    decrypt, get_message, preparation
import pytest


def test_decryption():
    """Testing decryption function."""
    assert decrypt('.... . .-.. .-.. --- | .-- --- .-. .-.. -..') == (
        'HELLO WORLD')
    assert decrypt('.---- ..--- ...-- ....- ..... -.... --... ---..') == (
        '12345678')
    assert decrypt('.-... .----. .--.-. -.--.- -.--. ---... --..--') == (
        "&'@)(:,")
    assert decrypt('... --- ...') == 'SOS'
    assert decrypt('... | --- | ...') == 'S O S'
    assert decrypt('... | | | | | --- | | | ...') == 'S     O   S'

    with pytest.raises(TypeError):
        decrypt('Hello World')
    with pytest.raises(TypeError):
        decrypt('...     ---  ...')
    with pytest.raises(TypeError):
        decrypt('$')


def test_encryption():
    """Testing encryption function."""
    assert encrypt('hello world') == ('.... . .-.. .-.. --- | .-- --- .-. '
                                      '.-.. -..')
    assert encrypt('12345678') == ('.---- ..--- ...-- ....- ..... -.... '
                                   '--... ---..')
    assert encrypt("&'@)(:,") == ('.-... .----. .--.-. -.--.- -.--. ---... '
                                  '--..--')
    assert encrypt('SOS') == '... --- ...'
    assert encrypt('S O S') == '... | --- | ...'
    assert encrypt('S     O   S') == '... | | | | | --- | | | ...'

    with pytest.raises(TypeError):
        encrypt('$')


def test_preparation():
    """Testing preparation function."""
    assert preparation('Hello      World') == ('Hello World', False)
    assert preparation(' Hello World ') == ('Hello World', False)
    assert preparation('...       ---   ...') == ('... | --- | ...', True)
    assert preparation("\"... --- ...\"") == (".-..-. ... --- ... .-..-.",
                                              True)


def test_continue_or_exit():
    """Testing continuity function."""
    assert continue_or_exit('YES') is False
    assert continue_or_exit('NO') is True


def test_copy_or_not():
    """Testing."""
    assert copy_or_not('NO') is None

    with pytest.raises(NameError):
        copy_or_not('YES')


def test_get_message():
    """Testing message insertion function."""
    assert get_message('hello') == 'hello'

    with pytest.raises(TypeError):
        get_message()
    with pytest.raises(OSError):
        get_message('$')
