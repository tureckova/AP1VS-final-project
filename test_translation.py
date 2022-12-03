"""TODO: docs."""
from translation import translate


def test_translate():
    """TODO: docs."""
    assert translate("Hellow world.", "cs") == "Ahoj světe."
    assert translate("Hellow world.", "e1m1") == "Neplatný jazyk výstupu."
    assert translate("Hellow world.", "cs", "e1m1") == \
           "Neplatný jazyk výstupu."
    assert translate("Das war ein Befehl!", "en", "de") == "This was an order!"
    assert translate("Amogus is great.", "cs", "auto") == "Amogus je skvělý."
