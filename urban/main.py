"""TerminalHasher.

A command-line utility for viewing cryptographic
translations of user defined passwords.
"""


import hashlib
"""Library with all the fancy hash functions"""


def encrypt_password(password, hash_type):
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

    print("You've chosen " + hash_type + " as your hash algorithm.")
    print("The hexadecimal value of this password is: " + result.hexdigest())
    print("Thanks, and don't forget to come again!")


def type_password():
    """type_password gets the user's password."""
    print("Please, enter your password(I won't look):")
    passwdinput = input()
    return passwdinput


def choose_algorithm():
    """Choose Algorithm returns chooses the hash algorithm."""
    print(
        "Please, choose your algorithm:\n"
        "[1 - SHA1 || 2 - SHA256 || 3 - SHA512 || 4 - MD5]\n"
    )
    count = input()

    typeos = ''

    match count:
        case "1":
            typeos = "sha1"
        case "2":
            typeos = "sha256"
        case "3":
            typeos = "sha512"
        case "4":
            typeos = "md5"
        case _:
            typeos = ''

    return typeos


def get_input(text):
    """get_input prints the user's input."""
    return input(text)


def intro():
    """Intro prints the welcome string."""
    print("Welcome to the best password hasher 2022")


if __name__ == '__main__':
    """Main function that runs everything."""
    intro()

    passwd = ''
    algorithm = ''

    while passwd == '':
        passwd = type_password()

    while algorithm == '':
        algorithm = choose_algorithm()

    encrypt_password(passwd, algorithm)
