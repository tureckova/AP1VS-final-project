"""Cryptographic password hashing."""

import hashlib


def HashPassw(hashChoice, passw, hsh):
    """
    Hashes the password via selected hash method.

    :param choice: Determines the hash algorithm (int)
    :param passw: The password to be hashed (string)
    :param hsh: Custom-made hash (string)
    :return: Hashed version of the password (string)
    """
    hashIt = passw + hsh
    if hashChoice == 1:
        hashed = hashlib.md5(hashIt.encode())
        return hashed.hexdigest()
    elif hashChoice == 2:
        hashed = hashlib.sha384(hashIt.encode())
        return hashed.hexdigest()
    elif hashChoice == 3:
        hashed = hashlib.sha512(hashIt.encode())
        return hashed.hexdigest()


def CheckInput(hashChoice):
    """
    Datatype and value check.

    :param uInput: Algorithm choice (string)
    """
    if hashChoice.isdigit():
        hashChoice = int(hashChoice)
        if hashChoice != 1 and hashChoice != 2 and hashChoice != 3:
            raise ValueError("Choose number 1, 2 or 3!!")
    else:
        raise TypeError("The input must be integer!!")


def CheckLength(passw, hsh):
    """
    User inputs length check.

    :param passw: Password to be hashed (string)
    :param hsh: Custom-made hash (string)
    """
    if len(passw) < 8:
        raise ValueError("Password should have 8 symbols or more!!")
    if len(hsh) < 5:
        raise ValueError("Hash should have 5 symbols or more!!")


if __name__ == "__main__":
    password = input("Password to hash (8 or more symbols): ")
    hash = input("Your own hash (5 or more symbols): ")
    algChoice = input("Choose algorith (1 = md5 ; 2 = sha384 ; 3 = sha512): ")

    CheckInput(algChoice)
    CheckLength(password, hash)

    print("\n\n")
    print("Hashed password: " + HashPassw(int(algChoice), password, hash))
    print("\n")
