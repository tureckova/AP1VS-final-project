import hashlib

def AlgorithmChoice(x):
    hashIt = password + hash
    if x == 1:
        hashed = hashlib.md5(hashIt.encode())
        return hashed.hexdigest()
    elif x == 2:
        hashed = hashlib.sha384(hashIt.encode())
        return hashed.hexdigest()
    elif x == 3:
        hashed = hashlib.sha512(hashIt.encode())
        return hashed.hexdigest()

def CheckInput():
    try:
        testInput = int(userInput)
        if testInput != 1 and testInput != 2 and testInput != 3:
            raise ValueError("Choose number 1, 2 or 3!!")
    except:
        raise TypeError("The input must be integer!!")

def CheckLength():
    if len(password) < 8:
        raise ValueError("Password should have 8 symbols or more!!")
    if len(hash) < 5:
        raise ValueError("Hash should have 5 symbols or more!!")


password = input("Password to hash (8 or more symbols): ")
hash = input("Your own hash (5 or more symbols): ")
userInput = input("Choose algorith (1 = md5 ; 2 = sha384 ; 3 = sha512): ")

CheckInput()
CheckLength()

print("-----------------------------------------------------------------------------------------------------------------------")
print("Hashed password: " + AlgorithmChoice(int(userInput)) + "\n")