CZECH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Generate MORSE_TO_CZECH from CZECH_TO_MORSE
MORSE_TO_CZECH = {}
for key, value in CZECH_TO_MORSE.items():
    MORSE_TO_CZECH[value] = key


def czech_to_morse(message):
    morse = []  # Will contain Morse versions of letters
    for char in message:
        if char in CZECH_TO_MORSE:
            morse.append(CZECH_TO_MORSE[char])
    return " ".join(morse)


def morse_to_czceh(message):
    message = message.split(" ")
    czech = []  # Will contain Czech versions of letters 
    for code in message:
        if code in MORSE_TO_CZECH:
            czech.append(MORSE_TO_CZECH[code])
    return " ".join(czech)


def main():
    while True:
        response = input("Convert Morse to Czech (1) or Czech to Morse (2)? ").upper()
        if response == "1" or response == "2":
            break

    if response == "1":
        print("Enter Morse code (with a space after each code): ")
        morse = input("> ")
        czech = morse_to_czceh(morse)
        print("### Czech version ###")
        print(czech)

    elif response == "2":
        print("Zadej Czech text: ")
        czech = input("> ").upper()
        morse = czech_to_morse(czech)
        print("### Morse Code version ###")
        print(morse)


if __name__ == "__main__":
    main()