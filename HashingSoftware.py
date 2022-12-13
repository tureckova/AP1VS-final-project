"""Cryptographic password hashing."""

import hashlib


def HashPassw(choice, passw, hsh):
    """
    Hashes the password via selected hash algorithm.

    :param choice: Determines the hash algorithm (int)
    :param passw: The password to be hashed (string)
    :param hsh: Custom-made hash (string)
    :return: Hashed version of the password (string)

    >>> HashPassw(1, "TezkeHeslo123", "SuperKratkyHash")
    '7e803bead7cfded9b43e1e5a9cfbf0fc'
    """
    hashIt = passw + hsh
    if choice == 1:
        hashed = hashlib.md5(hashIt.encode())
    elif choice == 2:
        hashed = hashlib.sha384(hashIt.encode())
    elif choice == 3:
        hashed = hashlib.sha512(hashIt.encode())
    return hashed.hexdigest()


def CheckInput(choice):
    """
    Datatype and value check.

    :param choice: Determines the hash algorithm (int)
    >>> CheckInput("a")
    Traceback (most recent call last):
    ...
    TypeError: The algorithm choice must be an integer!!
    """
    if choice.isdigit():
        choice = int(choice)
        if choice != 1 and choice != 2 and choice != 3:
            raise ValueError("Choose number 1, 2 or 3!!")
    else:
        raise TypeError("The algorithm choice must be an integer!!")


def CheckLength(passw, hsh):
    """
    User inputs length check.

    :param passw: The password to be hashed (string)
    :param hsh: Custom-made hash (string)
    """
    if len(passw) < 8:
        raise ValueError("Password should have 8 symbols or more!!")
    if len(hsh) < 5:
        raise ValueError("Hash should have 5 symbols or more!!")


if __name__ == "__main__":
    password = input("Password to hash (8 or more symbols): ")
    hash = input("Your own hash (5 or more symbols): ")
    algChoice = input("Choose algorithm (1 = md5 ; 2 = sha384 ; 3 = sha512): ")

    CheckInput(algChoice)
    CheckLength(password, hash)

    print("\n")
    print("Hashed password: " + HashPassw(int(algChoice), password, hash))
    print("\n")
