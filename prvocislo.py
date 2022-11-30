def primeNumber(x):
    y = 0
    if x <=0:
        print("Not valid input, please enter natural number")
        return
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
        answer=input("Enter another number?: y/n ")
        if answer=="y":
            primeNumber(x = int(input("Enter a number: ")))
        else:
            print("End of aplication") 
            break

primeNumber(x = int(input("Enter a number: ")))
odpoved()


