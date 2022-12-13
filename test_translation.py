"""Test module translation."""
from translation import translate, detect_language, is_valid_language


def test_translate():
    """Test for translation."""
    assert translate("Hellow world.", "cs") == "Ahoj světe."
    assert translate("Hellow world.", "e1m1") == "Neplatný jazyk výstupu."
    assert translate("Hellow world.", "cs", "e1m1") == "Neplatný jazyk vstupu."
    assert translate("Das war ein Befehl!", "en", "de") == "This was an order!"
    assert translate("Amogus is great.", "cs", "auto") == "Amogus je skvělý."
    assert translate(12345, "cs") == "Text musí být nenulový string."
    assert translate("", "en", "cs") == "Text musí být nenulový string."


def test_detect_language():
    """Test for detecting language."""
    assert detect_language("ahoj") == "Detekovaný jazyk: cs"
    assert detect_language("1") == "Detekovaný jazyk: en"
    assert detect_language(1235) == "Text musí být nenulový string."
    assert detect_language("     ") == "Text musí být nenulový string."
    assert detect_language("") == "Text musí být nenulový string."


def test_is_valid_language():
    """Test for checking if language is valid."""
    assert is_valid_language("cs")
    assert is_valid_language("", True)
    assert not is_valid_language("123")
    assert not is_valid_language(12345)
    assert not is_valid_language("123", True)
    assert not is_valid_language("")
