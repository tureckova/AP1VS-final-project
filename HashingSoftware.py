"""Cryptographic password hashing."""


import hashlib

def AlgorithmChoice(x, passw, hsh):
    hashIt = passw + hsh
    if x == 1:
        hashed = hashlib.md5(hashIt.encode())
        return hashed.hexdigest()
    elif x == 2:
        hashed = hashlib.sha384(hashIt.encode())
        return hashed.hexdigest()
    elif x == 3:
        hashed = hashlib.sha512(hashIt.encode())
        return hashed.hexdigest()

def CheckInput(uInput):
    try:
        testInput = int(uInput)
        if testInput != 1 and testInput != 2 and testInput != 3:
            raise ValueError("Choose number 1, 2 or 3!!")
    except:
        raise TypeError("The input must be integer!!")

def CheckLength(passw, hsh):
    if len(passw) < 8:
        raise ValueError("Password should have 8 symbols or more!!")
    if len(hsh) < 5:
        raise ValueError("Hash should have 5 symbols or more!!")

def main():
    password = input("Password to hash (8 or more symbols): ")
    hash = input("Your own hash (5 or more symbols): ")
    userInput = input("Choose algorith (1 = md5 ; 2 = sha384 ; 3 = sha512): ")

    CheckInput(userInput)
    CheckLength(password, hash)

    print("-----------------------------------------------------------------------------------------------------------------------")
    print("Hashed password: " + AlgorithmChoice(int(userInput), password, hash) + "\n")

main()
