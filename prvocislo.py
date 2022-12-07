"""Main module."""


def primeNumber(x):
    """Calc primeNumber value.

    :param x = entered number
    :return True
    Sample usage:
    >>> primeNumber(2)
    True

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


def odpoved(x):
    """Test type errors and input number."""
    if type(x) not in [int]:
        raise ValueError("Enter natural number")
    if x <= 0:
        raise TypeError("Number cant be lower or equal to 0")
    elif x == 1:
        raise TypeError("Cant be 1")
    z = primeNumber(x)
    if z:
        ans = "Prime number"
    else:
        ans = "Not a prime number"
    print(ans)
    return ans


def main():
    """Test of the entered answer."""
    x = int(input("Enter a number: "))
    odpoved(x)
    while True:
        answer = input("Enter another number?: y/n ")
        if answer == "y" or answer == "Y":
            x = int(input("Enter a number: "))
            odpoved(x)
        elif answer == "n" or answer == "N":
            print("End of application")
            break
        else:
            print("Choose y or n")


if __name__ == "__main__":
    main()
