"""Tests for main.py."""
import pytest
import builtins
from mainFile import * # noqa: F403


def test_minMax():
    """Testing minmax function."""
    assert minMax([5, 4, 7, 6, 2]) == (7, 2) # noqa: F405
    assert minMax([5, 2, 5, 1, 0]) == (5, 0) # noqa: F405
    assert minMax([-5, -2, -5, -1, 0]) == (0, -5) # noqa: F405
    assert minMax([5, -4, 7, -6, -2]) == (7, -6) # noqa: F405

    with pytest.raises(TypeError):
        minMax(["fgdf", 12, True, 5.4]) # noqa: F405
        minMax([12, 2.4, 4, 8]) # noqa: F405


def test_sort():
    """Testing sorting selection."""
    builtins.input = lambda: "1"
    result = sort([4, 2, 6, 5, 8]) # noqa: F405
    assert isinstance(result, list)

    for x in range(5):
        assert isinstance(result[x], int)


def test_bubbleSort():
    """Testing bubble sort algorithm."""
    assert bubbleSort([4, 2, 6, 5, 8]) == [2, 4, 5, 6, 8] # noqa: F405
    assert bubbleSort([5, 0, 4, 6, 12]) == [0, 4, 5, 6, 12] # noqa: F405
    assert bubbleSort([-4, -2, -6, -5, -8]) == [-8, -6, -5, -4, -2] # noqa: F405
    assert bubbleSort([-5, 0, 4, -6, 12]) == [-6, -5, 0, 4, 12] # noqa: F405

    with pytest.raises(TypeError):
        bubbleSort(["dfgh", 0, False, -6, 12.4]) # noqa: F405
        bubbleSort([15.2, 0, 5, 4, -4.1]) # noqa: F405


def test_insertionSort():
    """Testing insertion sort algorithm."""
    assert insertionSort([4, 2, 6, 5, 8]) == [2, 4, 5, 6, 8] # noqa: F405
    assert insertionSort([5, 0, 4, 6, 12]) == [0, 4, 5, 6, 12] # noqa: F405
    assert insertionSort([-4, -2, -6, -5, -8]) == [-8, -6, -5, -4, -2] # noqa: F405
    assert insertionSort([-5, 0, 4, -6, 12]) == [-6, -5, 0, 4, 12] # noqa: F405

    with pytest.raises(TypeError):
        insertionSort(["dfgh", 0, False, -6, 12.4]) # noqa: F405
        insertionSort([15.2, 0, 5, 4, -4.1]) # noqa: F405


def test_quickSort():
    """Testing quick sort algorithm."""
    assert quickSort([4, 2, 6, 5, 8]) == [2, 4, 5, 6, 8] # noqa: F405
    assert quickSort([5, 0, 4, 6, 12]) == [0, 4, 5, 6, 12] # noqa: F405
    assert quickSort([-4, -2, -6, -5, -8]) == [-8, -6, -5, -4, -2] # noqa: F405
    assert quickSort([-5, 0, 4, -6, 12]) == [-6, -5, 0, 4, 12] # noqa: F405

    with pytest.raises(TypeError):
        quickSort(["dfgh", 0, False, -6, 12.4]) # noqa: F405
        quickSort([15.2, 0, 5, 4, -4.1]) # noqa: F405


def test_documentInput():
    """Testing document input."""
    assert documentInput("project/testfiles/testfile.txt") ==\
           [5, 4, 7, 8, 9, 3, -4, 0, 1, 2] # noqa: F405
    assert documentInput("project/testfiles/testfile2.txt") ==\
           [5, 8, -4, 0, -2, -3, 1] # noqa: F405

    with pytest.raises(ValueError):
        assert documentInput("project/testfiles/testfile3.txt") # noqa: F405


def test_randomNumbers():
    """Testing that random numbers are numbers."""
    assert isinstance(randomNumbers(), list) # noqa: F405
    assert isinstance(randomNumbers()[2], int) # noqa: F405


def test_handleInputNumbers():
    """Testing that function returns numbers."""
    numbers = [4, 4, 6, -9]
    assert isinstance(handleInputNumbers(numbers), list) # noqa: F405

    for x in numbers:
        assert isinstance(x, int)
