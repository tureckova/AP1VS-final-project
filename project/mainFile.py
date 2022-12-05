# coding=utf-8

"""Script to sort numbers given by user, read in file or randomly assigned."""
import sys
import random


def inputType():
    """
    Decide on the type of input based on a number of parameters.

    :return:
    Returns numbers used in calculations
    """
    argumentsNumber = len(sys.argv)
    numbers = []

    # No argument provided by a user - random numbers
    if argumentsNumber == 1:
        numbers = sort(randomNumbers())

    # One argument provided - input from document
    elif argumentsNumber == 2:
        numbers = sort(documentInput(sys.argv[1]))

    # Multiple arguments provided - custom input
    elif argumentsNumber > 2:
        numbers = sort(handleInputNumbers(sys.argv[1:]))

    return numbers


def handleInputNumbers(numbers):
    """
    Save numbers to sort entered as arguments in a command line.

    :param number:
    Numbers in string data format

    :return:
    Returns an array of numbers

    >>> handleInputNumbers(['5', '4', '2'])
    Max number: 5 on index 0
    Min number: 2 on index 2
    <BLANKLINE>
    [5, 4, 2]
    """
    numbersInt = []
    for arg in numbers:
        numbersInt.append(int(arg))

    minMax(numbersInt)
    return numbersInt


def minMax(numbers):
    """
    Find the minimum and maximum in a collection.

    :param numbers:
    Array of numbers

    :return:
    Returns max and min number

    >>> minMax(['2', '1', '8'])
    Max number: 8 on index 2
    Min number: 1 on index 1
    <BLANKLINE>
    ('8', '1')
    """
    maxn = max(numbers)
    minn = min(numbers)
    print(f"Max number: {maxn} on index {numbers.index(maxn)}")
    print(f"Min number: {minn} on index {numbers.index(minn)}")
    print()
    return maxn, minn


def randomNumbers():
    """
    Generate 20 random numbers if no arguments are given by the user.

    :return:
    Returns randomly generated numbers in list
    """
    listNumbers = []
    for x in range(20):
        listNumbers.append(random.randint(0, 50))

    minMax(listNumbers)
    return listNumbers


def documentInput(fileName):
    """
    Pull out numbers from a file specified by a user.

    :param fileName:
    File name

    :return:
    Returns a list of numbers
    """
    with open(fileName) as f:
        contents = f.readline()

    intCollection = []

    for n in contents.split(" "):
        intCollection.append(int(n))

    minMax(intCollection)
    return intCollection


def sort(numbers):
    """
    Provide user with a choice of algorithms and sort numbers.

    :param numbers:
    Array of numbers

    :return:
    Returns a sorted list based on choice
    """
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
    """
    Sorting algorithm - Bubble sort.

    :param numbers:
    Array of numbers

    :return:
    Returns a sorted list

    >>> bubbleSort([2, 4, 7, 1])
    [1, 2, 4, 7]
    """
    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

    return numbers


def insertionSort(numbers):
    """
    Sorting algorithm - Insertion sort.

    :param numbers:
    Array of numbers

    :return:
    Returns a sorted list

    >>> insertionSort([2, 4, 7, 1])
    [1, 2, 4, 7]
    """
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers


def quickSort(numbers):
    """
    Sorting algorithm - Quick sort.

    :param numbers:
    Array of numbers

    :return:
    Returns a sorted list

    >>> quickSort([2, 4, 7, 1])
    [1, 2, 4, 7]
    """
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
    print()
    print(inputType())
