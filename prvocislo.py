from unittest import result


def primeNumber(x):
    """Calc primeNumber value.

    Sample usage:
    >>> primeNumber(2)
    True

    >>> primeNumber(True)
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: 'True'

    >>> primeNumber("5")
    Traceback (most recent call last):
    ...
    TypeError: Must be natural number

    >>> primeNumber(2.0)
    Traceback (most recent call last):
    ...
    ValueError: Must be natural number
    """
    y = 0
    if x <= 0 or x == 1:
        return False
    for i in range(2, x):
        if (x % i) == 0:
            y = 1
            break
    if y == 1:
        return False
    else:
        return True


def odpoved():
    while True:
        answer = input("Enter another number?: y/n ")
        if answer == "y" or answer == "Y":
            x = int(input("Enter a number: "))
            z = primeNumber(x)
            if z:
                print("Prime number")
            else:
                print("Not a prime number")
        elif answer == "n" or answer == "N":
            return ("End of application")
        else:
            print("Choose y or n")
            odpoved()
            break


if __name__ == "__main__":
    x = int(input("Enter a number: "))
    if x <= 0 or x == 1:
            print("Invalid input")
    else:
        r = primeNumber(x)
        if r:
            print("Prime number")
        else:
            print("Not a prime number")
    odpoved()
