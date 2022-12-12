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
    void = " "
    for i in s:  # indexování
        if i != ' ':
            void += dictionary[i]+" "
        else:
            void += ' '
    return void


def decoding(s):
    """Coding."""
    void = ""
    splitstring = s.split("  ")
    splitstring = s.split(" ")  # rozdělení podle mezer

    for i in splitstring:  # indexování
        void += dictionary2[i]
    return void


def main():
    """Return the pathname of the KOS root directory."""
    c = 1
    while (c != "0"):
        d = int(input("1.ČEŠTINY > MORSEOVKY|2.MORESOVKY > ČEŠTINY "))  # menu
        a = input("ZADEJ TEXT NA ŠIFROVÁNÍ: ")
        a = a.upper()
        if d == 1:  # šifrování
            print(coding(a))
        else:  # dešifrování
            print(decoding(a))


if __name__ == "__main__":
    main()
