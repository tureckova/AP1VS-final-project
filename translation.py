import googletrans
from googletrans import Translator
#vypsani dostupnych jazyku z knihovny
print('Tohle jsou všechny dostupné jazyky.')
print(googletrans.LANGUAGES)
translator = Translator()
#input part
srclan = input('Z jakého jazyka si přejete překládat? (nechte prázdné pro automatický překlad)')
destlan = input('Do jakého jazyka si přejete překládat?')
text = input('Co je text který chcete přeložit?: ')
#language detection
dt1 = translator.detect(text)
print(dt1)
#automaticky preklad
if srclan == '':
    #osetreni vstupu
    if destlan not in googletrans.LANGUAGES:
        destlan = input('Do jakého jazyka si přejete překládat? Zadejte platný jazyk z listu výše!')
    result = translator.translate(text, dest=destlan)
else:
    #osetreni vstupu
    if srclan not in googletrans.LANGUAGES:
        srclan = input('Z jakého jazyka si přejete překládat? Zadejte platný jazyk z listu výše! (nechte prázdné pro automatický překlad)')
    if destlan not in googletrans.LANGUAGES:
        destlan = input('Do jakého jazyka si přejete překládat? Zadejte platný jazyk z listu výše!')

    result = translator.translate(text, src=srclan, dest=destlan)

print(result.text)
