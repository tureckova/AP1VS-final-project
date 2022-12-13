import random
import sys

from FunkcePole import FunkcePole
import pytest


class TestFunkcePole():
    p = FunkcePole()

    def test_minimum(self):
        assert self.p.minimum([8, -8, 2]) == (-8, 2)

    def test_maximum(self):
         assert self.p.maximum([8, -8, 2]) == (8, 1)

    def test_nacteni_soubor(self):
        assert self.p.nacteni_soubor("cisla.txt") == [5,5]
        with pytest.raises(FileNotFoundError):
            assert self.p.nacteni_soubor("retra")
        with pytest.raises(ValueError):
            assert self.p.nacteni_soubor("text.txt")

    def test_nacteni_parametr(self):
        sys.argv = ["", "5", "4"]
        assert self.p.nacteni_parametr() == [5, 4]
        with pytest.raises(ValueError):
            sys.argv = ["", "nbdvcb", "gfh"]
            self.p.nacteni_parametr()

    def test_generovat(self):
        pole = self.p.generovat()
        assert len(pole) == 20 and all(isinstance(x, (int)) for x in pole)

    def test_pole(self):
        sys.argv = ["", "cisla.txt"]
        assert self.p.pole() == [5, 5]
        sys.argv = ["", "5", "4"]
        assert self.p.pole() == [5, 4]
        sys.argv = ["",]
        pole = self.p.pole()
        assert len(pole) == 20 and all(isinstance(x, (int)) for x in pole)


    class TestSort():
        s = FunkcePole.Sort()

        def test_bubble_sort(self):
            assert self.s.bubble_sort([8, -8, 2]) == [-8, 2, 8]

        def test_insertion_sort(self):
            assert self.s.insertion_sort([8, -8, 2]) == [-8, 2, 8]

        def test_selection_sort(self):
            assert self.s.selection_sort([8, -8, 2]) == [-8, 2, 8]
