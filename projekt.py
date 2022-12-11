"""Generating a joke of a specific category."""
import pyttsx3
import pyjokes


def speak(joke):
    """
    Print and read a joke.

    :param joke: Must be string

    Sample usage:
    speak(joke)
    joke
    speak(5)
    Traceback ( most receant call last):
    ...
    TypeError: Must be string.
    """
    if type(joke) not in [str]:
        raise TypeError("Must be string.")
    print(joke)
    computer = pyttsx3.init()
    computer.setProperty("rate", 150)
    computer.say(joke)
    computer.runAndWait()


def generateJoke(userInput):
    """
    Sort out userInput.

    :param userInput: Must be int

    Sample usage:
    generateJoke(True)
    Traceback ( most receant call last):
    ...
    TypeError: Must be predefined number.
    """
    if type(userInput) not in [int]:
        raise TypeError("Must be predefined number.")
    if userInput == 1:
        joke = pyjokes.get_joke(category="all")
    elif userInput == 2:
        joke = pyjokes.get_joke(category="chuck")
    elif userInput == 3:
        joke = pyjokes.get_joke(category="neutral")
    else:
        print("nezadal jsi číslo v rozmezí 1 - 3! ")
    return joke


def main(game):
    """
    Execute function.

    :param game: Must be boolean

    Sample usage:
    main(game)
    jakou kategorii vtipů chceš ?
    1 - all
    2 - chuck
    3 - neutral
    main(5)
    Traceback (most receant call last):
    ...
    TypeError: Must be (True, False).
    """
    if type(game) not in [bool]:
        raise TypeError("Must be (True, False).")
    while game:
        print("jakou kategorii vtipů chceš ?")
        print(" 1 - all \n" + " 2 - chuck\n" + " 3 - neutral")
        userInput = int(input())
        joke = generateJoke(userInput)
        speak(joke)
        uI = input("další vtip ?  press any key => ANO, press N => NE\n")
        if uI.upper() == "N":
            game = False

    print("Konec programu")


if __name__ == "__main__":
    main(True)
