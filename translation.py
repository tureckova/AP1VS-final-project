"""Translator project."""
from googletrans import LANGUAGES, LANGCODES, Translator

languages = list(LANGUAGES) + list(LANGCODES)
translator = Translator()


def translate(text, dest, src=""):
    """Translate given text.

    :param text: Text to translate
    :param dest: Language we're translating into
    :param src: Language we're translating from
    :return: Translated text

    >>> translate("Hello world.", "cs")
    'Ahoj světe.'
    >>> translate("Hello world.", "e1m1")
    'Neplatný jazyk výstupu.'
    >>> translate("Hello world.", "cs", "e1m1")
    'Neplatný jazyk vstupu.'
    """
    if not src.strip():
        src = "auto"
    if dest not in languages:
        return "Neplatný jazyk výstupu."
    if src not in languages and src != "auto":
        return "Neplatný jazyk vstupu."
    return translator.translate(text, src=src, dest=dest).text


def detect_language(text):
    """Detect language and Validate text input.

    :param text: Translated text
    :return: Output detected language
    """
    if type(text) is not str or not text.strip():
        return "Text musí být nenulový string."
    language = translator.detect(text)
    return f"Detekovaný jazyk: {language.lang}"


def is_valid_language(language, is_source=False):
    """Check if language parameter is in list of defined languages.

    :param language: Language from the list of languages
    :param is_source: If True, then empty string return true for auto-detection
    :return: Language validity
    """
    if language not in languages:
        if is_source and not language.strip():
            print("Jazyk bude automaticky rozpoznán.")
            return True
        print("Neplatný jazyk.")
        return False
    return True


def main():
    """Entry point when run as script."""
    # vypsani dostupnych jazyku z knihovny
    print("Tohle jsou všechny dostupné jazyky:"
          f"\n{LANGUAGES}")

    # set source language
    while not is_valid_language(
            srclan := input("Z jakého jazyka si přejete překládat?"
                            "(nechte prázdné pro automatický překlad)"), True):
        pass

    # set destination language
    while not is_valid_language(destlan := input("Do jakého jazyka si přejete překládat?")):  # noqa
        pass

    while type(srctext := input("Co je text který chcete přeložit?: ")) is not str or not srctext.strip():  # noqa
        print("Text musí být nenulový string.")

    # language detection
    if not srclan.strip():
        print(detect_language(srctext))

    print(translate(srctext, destlan, srclan))


if __name__ == "__main__":  # pragma: no cover
    """Executed if run as script."""
    main()
