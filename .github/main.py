from numpy import random
import sys
import os
import argparse

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


