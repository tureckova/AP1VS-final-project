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


    class TestSort():
        s = FunkcePole.Sort()

        def test_bubble_sort(self):
            assert self.s.bubble_sort([8, -8, 2]) == [-8, 2, 8]

        def test_insertion_sort(self):
            assert self.s.insertion_sort([8, -8, 2]) == [-8, 2, 8]

        def test_selection_sort(self):
            assert self.s.selection_sort([8, -8, 2]) == [-8, 2, 8]
