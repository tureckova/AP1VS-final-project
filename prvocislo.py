def number():
    x = int(input("Enter a number: "))
    while x <= 0:
        x = int(input("Enter a number: "))
    return x

def test_number(x):
    y = 0
    for i in range(2,x):
        if (x%i)==0:
            y = 1
            break
    if y == 1:
        print(x, "Not a prime number")
    else:   
        print(x, "Prime number")
def odpoved():   
    while True:
        answer=input("One time next time?: y/n ")
        if answer=="y":
            test_number(x = int(input("Enter a number: ")))
        else:
            print("End of aplication") 
            break

test_number(number())
odpoved()


