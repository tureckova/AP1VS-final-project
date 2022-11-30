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

password = input("Password to hash: ")
hash = input("Your own hash: ")
x = input("Choose algorith (1 = md5 ; 2 = sha384 ; 3 = sha512): ")

print("-----------------------------------------------------------------------------------------------------------------------")
print("Hashed password: " + AlgorithmChoice(int(x)) + "\n")