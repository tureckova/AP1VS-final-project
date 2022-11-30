def primeNumber(x):
    y = 0
    for i in range(2,x):
        if (x%i)==0:
            y = 1
            break
    if y == 1:
        print(x, "nie je prvocislo")
    else:
        print(x, "je prvocislo")
primeNumber(x=int(input("Zadaj cislo: ")))


def odpoved():   
    while True:
        answer=input("Chces zadat dalsie cislo? ano/nie: ")
        if answer=="ano":
            primeNumber(x=int(input("Zadaj cislo: ")))
        else:
            print("Koniec programu") 
        break
odpoved()

