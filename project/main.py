import sys
import random

def inputType():
    argumentsNumber = len(sys.argv)

    if argumentsNumber == 1:
        randomNumbers()
    elif argumentsNumber == 2:
        documentInput()
    elif argumentsNumber > 2:
        handleInputNumbers()


def handleInputNumbers():
    numbers = []
    for arg in sys.argv[1:]:
        numbers.append(int(arg))

    return numbers


def randomNumbers():
    listNumbers = []
    for x in range(20):
        listNumbers.append(random.randint(0, 50))

    return listNumbers


def documentInput():
    with open(sys.argv[1]) as f:
        contents = f.readline()

    intCollection = []

    for n in contents.split(" "):
        intCollection.append(int(n))

    print(intCollection)
    return intCollection


if __name__ == '__main__':
    inputType()
