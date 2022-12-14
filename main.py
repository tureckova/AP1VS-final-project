"""Projekt MinMax."""
from FunkcePole import FunkcePole

f = FunkcePole()
s = f.Sort()
x = f.pole()


nejmensi = f.minimum(x)
nejvetsi = f.maximum(x)

s.vyber_sortu(x)
