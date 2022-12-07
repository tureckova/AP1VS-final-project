"""Translator project."""
from googletrans import LANGUAGES, LANGCODES, Translator

languages = list(LANGUAGES) + list(LANGCODES)
translator = Translator()


def translate(text, dest, src="auto"):
    """Translate given text.

    :param text:
    :param dest:
    :param src:
    :return:

    >>> translate("Hello world.", "cs")
    'Ahoj světe.'
    >>> translate("Hello world.", "e1m1")
    'Neplatný jazyk výstupu.'
    >>> translate("Hello world.", "cs", "e1m1")
    'Neplatný jazyk výstupu.'
    """
    if dest not in languages:
        return "Neplatný jazyk výstupu."
    if src not in languages and src != "auto":
        return "Neplatný jazyk výstupu."
    return translator.translate(text, src=src, dest=dest).text


def detect_language(text):
    """TODO.

    :param text:
    :return:
    """
    if type(text) is not str or not text.strip():
        return "Text musí být nenulový string."
    language = translator.detect(text)
    return f"Detekovaný jazyk: {language.lang}"


def is_valid_language(language):
    """TODO.

    :param language:
    :return:
    """
    if language not in languages:
        print("Neplatný jazyk.")
        return False
    return True


def get_source_language():  # pragma: no cover
    """Get source language.

    Receive source language from which to translate

    :return:
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


def main():
    """Entry point when run as script."""
    # vypsani dostupnych jazyku z knihovny
    print("Tohle jsou všechny dostupné jazyky:"
          f"\n{LANGUAGES}")

    # set source language
    srclan = get_source_language()
    # set destination language
    while not is_valid_language(destlan := input("Do jakého jazyka si přejete překládat?")):  # noqa
        pass

    while type(srctext := input("Co je text který chcete přeložit?: ")) is not str or not srctext.strip():  # noqa
        print("Text musí být nenulový string.")

    # language detection
    if srclan == "auto":
        print(detect_language(srctext))

    print(translate(srctext, destlan, srclan))


if __name__ == "__main__":  # pragma: no cover
    """Executed if run as script."""
    main()
