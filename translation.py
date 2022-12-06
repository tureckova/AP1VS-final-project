"""Translator project."""
from googletrans import LANGUAGES, LANGCODES, Translator

languages = list(LANGUAGES) + list(LANGCODES)
translator = Translator()


def translate(text, dest, src="auto"):
    """Translate given text.

    >>> translate("Hellow world.", "cs")
    Ahoj světe.
    >>>translate("Hellow world.", "e1m1")
    Neplatný jazyk výstupu.
    >>>translate("Hellow world.", "cs", "e1m1")
    Neplatný jazyk výstupu.
    """
    if dest not in languages:
        return "Neplatný jazyk výstupu."
    if src not in languages and src != "auto":
        return "Neplatný jazyk výstupu."
    return translator.translate(text, src=src, dest=dest).text


def get_source_language():  # pragma: no cover - TODO
    """Get source language.

    Receive source language from which to translate
    TODO: unit test
    """
    language = input("Z jakého jazyka si přejete překládat? "
                     "(nechte prázdné pro automatický překlad)")
    if language == '':
        return 'auto'
    while language not in languages:
        language = input("Z jakého jazyka si přejete překládat? "
                         "Zadejte platný jazyk z listu výše! "
                         "(nechte prázdné pro automatický překlad)")
    return language


def get_destination_language():  # pragma: no cover - TODO
    """Get destination language.

    Receive destination language to which to translate

    TODO: unit test
    """
    language = input("Do jakého jazyka si přejete překládat?")
    while language not in languages:
        language = input("Do jakého jazyka si přejete překládat? "
                         "Zadejte platný jazyk z listu výše!")
    return language


def main():
    """Entry point when run as script."""
    # vypsani dostupnych jazyku z knihovny
    print("Tohle jsou všechny dostupné jazyky.")
    print(LANGUAGES)

    # input part
    srclan = get_source_language()
    destlan = get_destination_language()
    srctext = input("Co je text který chcete přeložit?: ")

    # language detection
    if srclan == "auto":
        print(translator.detect(srctext))

    print(translate(srctext, destlan, srclan))


if __name__ == "__main__":
    """Executed if run as script."""
    main()
