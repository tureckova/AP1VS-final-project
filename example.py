"""Morse code."""

dictionary = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..', }

dictionary2 = {'.-': 'A', '-...': 'B', '-.-.': 'C',
               '-..': 'D', '.': 'E', '..-.': 'F',
               '--.': 'G', '....': 'H',
               '..': 'I', '.---': 'J',
               '-.-': 'K', '.-..': 'L',
               '--': 'M', '-.': 'N',
               '---': 'O', '.--.': 'P', '--.-': 'Q',
               '.-.': 'R', '...': 'S', '-': 'T',
               '..-': 'U', '...-': 'V', '.--': 'W',
               '-..-': 'X', '-.--': 'Y', '--..': 'Z', '': ' ', }


def coding(s):
    """Coding."""
    void = ""
    for i in s:  # indexování
        if i != ' ':
            void += dictionary[i]+' '
        else:
            void += ' '

    print(void)


def decoding(s):
    """Coding."""
    void = ""
    splitstring = s.split("  ")
    splitstring = s.split(" ")  # rozdělení podle mezer

    for i in splitstring:  # indexování
        void += dictionary2[i]

    print(void)


def selection(f):
    """Return the pathname of the KOS root directory."""
    f = int(input("1.ČEŠTINA > MORSEOVKA || 2.MORESOVKA > ČEŠTINA "))  # menu
    return f


c = 1
d = 0
while (c != "0"):
    d = selection(d)
    a = input("ZADEJ TEXT NA ŠIFROVÁNÍ: ")
    a = a.upper()

    startUp = ""  # nevyužívá se ale bez ní program nelze spustit

    if d == 1:  # šifrování
        coding(a)

    else:  # dešifrování
        decoding(a)

c = input(("PROGRAM SE UKONČI=0 || POKRAČOVÁNÍ=LIBOVOLNÝ ZNAK : "))


