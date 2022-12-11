from numpy import random
import sys
import os


def generovatNahodnePole():
    nahodnePole=random.randint(1000, size=(20))
    novePole=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in range (20):
        novePole[x]=nahodnePole[x]
    return novePole

def parametrovePole():
    try:
        parametrovePole = [int(i) for i in sys.argv[1:]]
    except:
        raise ValueError("nelze převést na int")
    return parametrovePole

def nacteniZeSouboru(path):
    if not os.path.isfile(path):
        raise FileNotFoundError("soubor neexistuje")
    with open(path) as f:
        try:
            polezesouboru = [int(i) for i in f.readline()]
        except:
            raise ValueError("nelze převést na int")
    return  polezesouboru

def pole():
    if len(sys.argv) == 1:
        pole = generovatNahodnePole()
    elif len(sys.argv) == 2:
        pole = nacteniZeSouboru(sys.argv[1])
    else:
        pole = parametrovePole()
    return pole

def maximum(pole):
    hodnotaMax=max(pole)
    return hodnotaMax,pole.index(hodnotaMax)

def minimum(pole):
    hodnotaMin = min(pole)
    return hodnotaMin, pole.index(hodnotaMin)

class sort:

    def vyberSortu(pole):
        print(".....\nVyberte si serazovaci algoritmus:\nb = bubbleSort\ni = insertionSort\ns = selectionSort\n.....")
        x = input()
        if x == "b":
            sort.bubbleSort(pole)
            print(pole)
        elif x == "i":
            sort.insertionSort(pole)
            print(pole)
        elif x == "s":
            sort.selectionSort(pole)
            print(pole)
        else:
            print("spatna volba")

    def bubbleSort(pole):
        n = len(pole)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if pole[j] > pole[j + 1]:
                    pole[j], pole[j + 1] = pole[j + 1], pole[j]

    def insertionSort(pole):
        for i in range(1, len(pole)):
            cislo = pole[i]
            j = i - 1
            while j >= 0 and cislo < pole[j]:
                pole[j + 1] = pole[j]
                j -= 1
            pole[j + 1] = cislo

    def selectionSort(pole):
        for i in range(0, len(pole) - 1):
            p = 0
            mini = pole[-1]
            for j in range(i, len(pole)):
                if pole[j] <= mini:
                    mini = pole[j]
                    p = j
            pole[i], pole[p] = pole[p], pole[i]







test=pole()
sort.vyberSortu(test)






