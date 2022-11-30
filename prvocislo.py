def primeNumber(x):
    """Calc Uloha value.
    
    Sample usage:
    >>> primeNuber(1)
    "Not valid input, please enter natural number"
    
    >>> primeNuber(2)
    "Prime number"
    
    >>> primeNuber(-10)
    "Not valid input, please enter natural number"
    
    >>> primeNuber(True)
    Traceback (most recent call last):
    ...
    TypeError: Must be natural number
    
    >>> primeNuber("5")
    Traceback (most recent call last):
    ...
    TypeError: Must be natural number
    
    >>> primeNumber(2.0)
    Traceback (most recent call last):
    ...
    ValueError: Must be natural number
     
    >>> primeNumber(-2.1)
    Traceback (most recent call last):
    ...
    ValueError: Must be natural number

    >>> primeNumber(2,5) 
    Traceback (most recent call last):
    ...
    ValueError: Must be natural number
    """
    y = 0
    if x <=0 or x==1:
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


