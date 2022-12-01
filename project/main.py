import sys
import random

def inputType():
    argumentsNumber = len(sys.argv)

    if argumentsNumber == 1:
        randomNumbers()
    elif argumentsNumber == 2:
        print("document")
    elif argumentsNumber > 2:
        handleInputNumbers()


def handleInputNumbers():
    numbers = []
    for arg in sys.argv[1:]:
        numbers.append(int(arg))

    return numbers


def randomNumbers():
    listNumbers = []
    for x in range(21):
        listNumbers.append(random.randint(0, 50))

    return listNumbers


def documentInput():
    print()


if __name__ == '__main__':
    inputType()
