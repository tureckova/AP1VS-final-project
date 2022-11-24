import hashlib

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

    print("The hexadecimal value of this password is: " + result.hexdigest())
    print("Thanks, and don't forget to come again!")


def TypePassword():
    print("Please, enter your password(I won't look):")
    passwdinput = input()
    return passwdinput


def ChooseAlgorithm():
    print("Please, choose your algorithm:\n")
    count = input()

    match count:
        case "1":
            typeos = "sha1"
        case "2":
            typeos = "sha256"
        case "3":
            typeos = "sha512"
        case "4":
            typeos = "md5"

    return typeos


def Intro():
    print("Welcome to the best password hasher 2022")


if __name__ == '__main__':
    Intro()
    passwd = TypePassword()
    algorithm = ChooseAlgorithm()
    print(passwd)
    print(algorithm)
    EncryptPassword(passwd, algorithm)
