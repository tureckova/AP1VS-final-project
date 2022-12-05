"""Tests for main.py."""
import pytest
import builtins
from main import minMax
from main import bubbleSort
from main import insertionSort
from main import quickSort
from main import sort
from main import documentInput
from main import randomNumbers
from main import handleInputNumbers


def test_minMax():
    """Testing minmax function."""
    assert minMax([5, 4, 7, 6, 2]) == (7, 2)
    assert minMax([5, 2, 5, 1, 0]) == (5, 0)
    assert minMax([-5, -2, -5, -1, 0]) == (0, -5)
    assert minMax([5, -4, 7, -6, -2]) == (7, -6)

    with pytest.raises(TypeError):
        minMax(["fgdf", 12, True, 5.4])
        minMax([12, 2.4, 4, 8])


def test_bubbleSort():
    """Testing bubble sort algorithm."""
    assert bubbleSort([4, 2, 6, 5, 8]) == [2, 4, 5, 6, 8]
    assert bubbleSort([5, 0, 4, 6, 12]) == [0, 4, 5, 6, 12]
    assert bubbleSort([-4, -2, -6, -5, -8]) == [-8, -6, -5, -4, -2]
    assert bubbleSort([-5, 0, 4, -6, 12]) == [-6, -5, 0, 4, 12]

    with pytest.raises(TypeError):
        bubbleSort(["dfgh", 0, False, -6, 12.4])
        bubbleSort([15.2, 0, 5, 4, -4.1])


def test_insertionSort():
    """Testing insertion sort algorithm."""
    assert insertionSort([4, 2, 6, 5, 8]) == [2, 4, 5, 6, 8]
    assert insertionSort([5, 0, 4, 6, 12]) == [0, 4, 5, 6, 12]
    assert insertionSort([-4, -2, -6, -5, -8]) == [-8, -6, -5, -4, -2]
    assert insertionSort([-5, 0, 4, -6, 12]) == [-6, -5, 0, 4, 12]

    with pytest.raises(TypeError):
        insertionSort(["dfgh", 0, False, -6, 12.4])
        insertionSort([15.2, 0, 5, 4, -4.1])


def test_quickSort():
    """Testing quick sort algorithm."""
    assert quickSort([4, 2, 6, 5, 8]) == [2, 4, 5, 6, 8]
    assert quickSort([5, 0, 4, 6, 12]) == [0, 4, 5, 6, 12]
    assert quickSort([-4, -2, -6, -5, -8]) == [-8, -6, -5, -4, -2]
    assert quickSort([-5, 0, 4, -6, 12]) == [-6, -5, 0, 4, 12]

    with pytest.raises(TypeError):
        quickSort(["dfgh", 0, False, -6, 12.4])
        quickSort([15.2, 0, 5, 4, -4.1])


def test_sort():
    """Testing sorting selection."""
    builtins.input = lambda: "1"
    result = sort([4, 2, 6, 5, 8])
    assert isinstance(result, list)

    for x in range(5):
        assert isinstance(result[x], int)


def test_documentInput():
    """Testing document input."""
    assert documentInput("project/testfiles/testfile.txt") ==\
           [5, 4, 7, 8, 9, 3, -4, 0, 1, 2]
    assert documentInput("project/testfiles/testfile2.txt") ==\
           [5, 8, -4, 0, -2, -3, 1]

    with pytest.raises(ValueError):
        assert documentInput("project/testfiles/testfile3.txt")


def test_randomNumbers():
    """Testing that random numbers are numbers."""
    assert isinstance(randomNumbers(), list)
    assert isinstance(randomNumbers()[2], int)


def test_handleInputNumbers():
    """Testing that function returns numbers."""
    numbers = [4, 4, 6, -9]
    assert isinstance(handleInputNumbers(numbers), list)

    for x in numbers:
        assert isinstance(x, int)
