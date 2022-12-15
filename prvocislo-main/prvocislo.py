"""Primality testing."""
from math import sqrt
import random


# https://en.wikipedia.org/wiki/Fermat%27s_factorization_method


def type_prime(input):
    """
    Say if input is prime.

    Check input and pass on to counting_prime, returns only bool
    >>> type_prime(2)
    True
    >>> type_prime(4)
    False
    >>> type_prime(-3)
    False
    >>> type_prime(7.0)
    True
    >>> type_prime(7.1)
    False
    >>> type_prime("5")
    True
    >>> type_prime("6")
    False
    >>> type_prime("abc")
    False
    >>> type_prime(True)
    False
    """
    match input:
        case int():
            return counting_prime(input)
        case float():
            return counting_prime(input)
        case str():
            try:
                return counting_prime(float(input))
            except ValueError:
                return False  # not a number
        case _:
            return False  # not a number


def counting_prime(input):
    """
    Give primality of number.

    Checks size, bruteforces, or passes to is_prime
    >>> counting_prime(2)
    True
    >>> counting_prime(4)
    False
    >>> counting_prime(-3)
    False
    >>> counting_prime(7.0)
    True
    >>> counting_prime(7.1)
    False
    """
    # if whole number
    if (input == int(input)):
        if (input > 100_000_000):
            return is_prime(input, 3)
        if (input % 2 == 0):
            return False
        for i in range(3, int(sqrt(input) + 1), 2):
            # no need to count to input
            # biggest not yet tested prime divider is square root of input
            if (input % i == 0):
                return False
        return True
    # Non whole numbers cannot be prime
    return False


# Fermat's factorization method
def power(a, p):
    """
    Don't return 1 if number isn't prime.

    Can, and does, return 1 if number isn't prime
    >>> power(2,12)
    8
    >>> power(2,13)
    1
    >>> power(3,15)
    9
    """
    # Initialize result
    result = 1
    n = p - 1
    # Remove every p from a
    a = a % p
    while n > 0:
        # If n is odd, multiply 'a' with result
        if n % 2:
            result = (result * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
            # n must be even now
            n = n // 2
    return result % p


# If n is prime, then always returns true,
# If n is composite than returns false with
# high probability Higher value of k increases
# probability of correct result
def is_prime(n, k):
    """
    Try primality heuristically k times.

    Tries a new random number each time
    >>> is_prime(2,3)
    True
    >>> is_prime(4,5)
    False
    >>> is_prime(-3,2)
    False
    >>> is_prime(7.0,3)
    True
    >>> is_prime(7.1,3)
    False
    """
    # Corner cases
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    # Try k times
    else:
        for i in range(k):
            # Pick a random number in [2..n-2]
            # sure that n > 4
            a = random.randint(2, n - 2)
            # Fermat's little theorem
            if power(a, n) != 1:
                return False
    return True
    
if __name__ == "__main__":
    repeat = "y"
    while (repeat == "y"):
        n = input("Enter a whole number: ")
        if (type_prime(n)):
            print(n + " is a whole number")
        else:
            print(n + " is not a whole number")
        repeat = input("Wish to test another number? Type y: ")

