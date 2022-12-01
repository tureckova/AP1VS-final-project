import sys
import random

def inputType():
    argumentsNumber = len(sys.argv)

    if argumentsNumber == 1:
        return sort(randomNumbers())
    elif argumentsNumber == 2:
        return sort(documentInput())
    elif argumentsNumber > 2:
        return sort(handleInputNumbers())


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


def sort(numbers):
    print("Select sort algorithm:")
    print("1 - Quick sort")
    print("2 - Insertion sort")
    print("3 - Bubble sort")

    choice = input()

    if choice == "1":
        return quickSort(numbers)
    elif choice == "2":
        return insertionSort(numbers)
    elif choice == "3":
        return bubbleSort(numbers)


def bubbleSort(numbers):
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers


def insertionSort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers


def quickSort(numbers):
    less = []
    equal = []
    greater = []

    if len(numbers) > 1:
        pivot = numbers[0]
        for x in numbers:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        return quickSort(less)+equal+quickSort(greater)
    else:
        return numbers


if __name__ == '__main__':
    print(inputType())
