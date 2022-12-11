"""TerminalHasher.

A command-line utility for viewing cryptographic
translations of user defined passwords.
"""

import hashlib
"""Library with all the fancy hash functions."""


def get_input(text):
    """get_input prints the user's input."""
    if text is None:
        return input()
    else:
        return text


def encrypt_password(password, hash_type, only_return=False):
    """encrypt_password encrypts the given password and returns the hash."""
    match hash_type:
        case "md5":
            result = hashlib.md5(password.encode())
        case "sha1":
            result = hashlib.sha1(password.encode())
        case "sha256":
            result = hashlib.sha256(password.encode())
        case "sha512":
            result = hashlib.sha512(password.encode())
        case _:
            print("Funny non existent hash algorithm detected.")
            return

    if only_return:
        return result.hexdigest()

    print("You've chosen " + hash_type + " as your hash algorithm.")
    print("The hexadecimal value of this password is: " + result.hexdigest())
    print("Thanks, and don't forget to come again!")


def type_password(password_example):
    """type_password gets the user's input."""
    print("Please, enter your password(I won't look):")
    if password_example is None:
        passwd_input = get_input(None)
        return passwd_input
    else:
        return password_example


def choose_algorithm(count_input):
    """choose_algorithm chooses the hashing Algorithm.
    User input can be 1,2,3,4.  """
    print(
        "Please, choose your algorithm:\n"
        "[1 - SHA1 || 2 - SHA256 || 3 - SHA512 || 4 - MD5]\n"
    )

    if count_input is None:
        count = get_input(None)
    else:
        count = count_input

    match count:
        case "1":
            hash_type = "sha1"
        case "2":
            hash_type = "sha256"
        case "3":
            hash_type = "sha512"
        case "4":
            hash_type = "md5"
        case _:
            hash_type = ''

    return hash_type


def intro():
    """Intro prints the initial string."""
    print("Welcome to the best password hasher 2022")


if __name__ == '__main__':
    """Launches methods to run program."""
    intro()

    passwd = ''
    algorithm = ''

    while passwd == '':
        passwd = type_password(None)

    while algorithm == '':
        algorithm = choose_algorithm(None)

    encrypt_password(passwd, algorithm)
