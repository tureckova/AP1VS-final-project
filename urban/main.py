import hashlib

"""
A command-line utility for viewing cryptographic translations of user defined passwords.
"""
def EncryptPassword(passwd, type):
    match type:
        case "md5":
            result = hashlib.md5(passwd.encode())
        case "sha1":
            result = hashlib.sha1(passwd.encode())
        case "sha256":
            result = hashlib.sha256(passwd.encode())
        case "sha512":
            result = hashlib.sha512(passwd.encode())
        case _:
            print("Funny non existent hash algorithm detected.")
            return

    print("You've chosen " + type + " as your hash algorithm.")
    print("The hexadecimal value of this password is: " + result.hexdigest())
    print("Thanks, and don't forget to come again!")


def TypePassword():
    print("Please, enter your password(I won't look):")
    passwdinput = input()
    return passwdinput


def ChooseAlgorithm():
    print("Please, choose your algorithm:\n[1 - SHA1 || 2 - SHA256 || 3 - SHA512 || 4 - MD5]\n")
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


def Intro():
    """Prints the welcome string."""
    print("Welcome to the best password hasher 2022")


if __name__ == '__main__':
    Intro()

    passwd = ''
    algorithm = ''

    while passwd == '':
        passwd = TypePassword()

    while algorithm == '':
        algorithm = ChooseAlgorithm()

    EncryptPassword(passwd, algorithm)
