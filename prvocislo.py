def primeNumber(x):
    """Calc primeNumber value.

    Sample usage:
    >>> primeNumber(1)
    "Not valid input, please enter natural number"

    >>> primeNumber(2)
    "Prime number"

    >>> primeNumber(-10)
    "Not valid input, please enter natural number"

    >>> primeNumber(True)
    Traceback (most recent call last):
    ...
    ValueError: Must be natural number

    >>> primeNumber("5")
    Traceback (most recent call last):
    ...
    TypeError: Must be natural number

    >>> primeNumber(2.0)
    Traceback (most recent call last):
    ...
    ValueError: Must be natural number

    >>> primeNumber(-2.1)
    Traceback (most recent call last):
    ...
    ValueError: Must be natural number

    >>> primeNumber(2,5)
    Traceback (most recent call last):
    ...
    ValueError: Must be natural number

    >>> primeNumber(5-2)
    Traceback (most recent call last):
    ...
    ValueError: Must be natural number
    """
    y = 0
    if x <= 0 or x == 1:
        return ("Not valid input, please enter natural number")
    for i in range(2, x):
        if (x % i) == 0:
            y = 1
            break
    if y == 1:
        return (x, "Not a prime number")
    else:
        return (x, "Prime number")


def odpoved():
    while True:
        answer = input("Enter another number?: y/n ")
        if answer == "y" or answer == "Y":
            x = int(input("Enter a number: "))
            print(primeNumber(x))
        elif answer == "n" or answer == "N":
            return ("End of application")
        else:
            print("Choose y or n")
            odpoved()
            break


if __name__ == "__main__":
    x = int(input("Enter a number: "))
    print(primeNumber(x))
    odpoved()
