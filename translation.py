"""TODO: docs."""
import googletrans
from googletrans import Translator


def get_source_language():
    """TODO: docs."""
    language = input("Z jakého jazyka si přejete překládat? "
                     "(nechte prázdné pro automatický překlad)")
    if language == '':
        return language
    while not (language in googletrans.LANGUAGES or
               language in googletrans.LANGUAGES.values()):
        language = input("Z jakého jazyka si přejete překládat? "
                         "Zadejte platný jazyk z listu výše! "
                         "(nechte prázdné pro automatický překlad)")
    return language


def get_destination_language():
    """TODO: docs."""
    language = input("Do jakého jazyka si přejete překládat?")
    while not (language in googletrans.LANGUAGES or
               language in googletrans.LANGUAGES.values()):
        language = input("Do jakého jazyka si přejete překládat? "
                         "Zadejte platný jazyk z listu výše!")
    return language


"""vypsani dostupnych jazyku z knihovny"""
print("Tohle jsou všechny dostupné jazyky.")
print(googletrans.LANGUAGES)
translator = Translator()

"""input part"""
srclan = get_source_language()
destlan = get_destination_language()
text = input("Co je text který chcete přeložit?: ")

"""language detection"""
dt1 = translator.detect(text)
print(dt1)

"""automaticky preklad"""
if srclan == '':
    result = translator.translate(text, dest=destlan)
else:
    result = translator.translate(text, src=srclan, dest=destlan)

print(result.text)
