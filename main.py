"""Projekt MinMax."""
from FunkcePole import FunkcePole

f = FunkcePole()
s = f.Sort()
x = f.pole()
print("Vase pole je:\n", x, "\n")

nejmensi = f.minimum(x)
nejvetsi = f.maximum(x)
print("Nejmensi cislo je ",
      nejmensi[0],
      " a nachazi se na pozici ",
      nejmensi[1])
print("Nejvetsi cislo je ",
      nejvetsi[0],
      " a nachazi se na pozici ",
      nejvetsi[1],
      "\n")

s.vyber_sortu(x)