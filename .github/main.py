from numpy import random
import sys

def generovatNahodnePole():
    nahodnePole=random.randint(1000, size=(20))
    novePole=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in range (20):
        novePole[x]=nahodnePole[x]
    return novePole

def parametrovePole():
    parametrovePole=sys.argv[1:]
    sys.argv[1:]
    if type(parametrovePole) not in [int, float]:
        raise TypeError("není int, ani float")
    return parametrovePole
def pole():
    pole=generovatNahodnePole()
    return pole
def maximum(pole):
    hodnotaMax=max(pole)
    return hodnotaMax,pole.index(hodnotaMax)

def minimum(pole):
    hodnotaMin = min(pole)
    return hodnotaMin, pole.index(hodnotaMin)



