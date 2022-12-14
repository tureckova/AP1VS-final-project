Morse_dictionary = {
    'a': '.-', 'b': '-...', 'c': '-.-.',
    'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'ch': '----',
    'i': '..', 'j': '.---', 'k': '-.-',
    'l': '.-..', 'm': '--', 'n': '-.',
    'o': '---', 'p': '.--.', 'q': '--.-',
    'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--',
    'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/', '': ''
}
def encrypt(translate):
    text = ''
    for letter in translate:
        text += Morse_dictionary[letter] + ' '
    return text

def decrypt(translate):
    global n
    promena = ''
    translate += ' '
    word = ''

    for letter in translate:

        if letter != ' ':
            n = 0
            promena += letter

        else:
            n += 1
            if n == 2:
                word += ' '
            else:
                word += list(Morse_dictionary.keys())[list(
                    Morse_dictionary.values()).index(promena)]
                promena = ''
    return word
