"""TODO: docs."""
import googletrans
from googletrans import Translator


def translate(text, dest, src="auto"):
    """TODO: docs.

    TODO: unit test
    """
    if dest not in languages:
        return "Neplatný jazyk výstupu."
    if src not in languages and src != "auto":
        return "Neplatný jazyk výstupu."
    return translator.translate(text, src=src, dest=dest).text


def get_source_language():
    """TODO: docs.

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


def get_destination_language():
    """TODO: docs.

    TODO: unit test
    """
    language = input("Do jakého jazyka si přejete překládat?")
    while language not in languages:
        language = input("Do jakého jazyka si přejete překládat? "
                         "Zadejte platný jazyk z listu výše!")
    return language


"""vypsani dostupnych jazyku z knihovny"""
print("Tohle jsou všechny dostupné jazyky.")
print(googletrans.LANGUAGES)
languages = list(googletrans.LANGUAGES) + list(googletrans.LANGCODES)
translator = Translator()

"""input part"""
srclan = get_source_language()
destlan = get_destination_language()
srctext = input("Co je text který chcete přeložit?: ")

"""language detection"""
if srclan == "auto":
    print(translator.detect(srctext))

print(translate(srctext, destlan, srclan))
