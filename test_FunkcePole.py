"""unit testy"""
import sys
from FunkcePole import FunkcePole
import pytest


class TestFunkcePole:
    """třída por otestování funkcí pole"""
    p = FunkcePole()

    def test_minimum(self):
        """test funkce minimum"""
        assert self.p.minimum([8, -8, 2]) == (-8, 2)

    def test_maximum(self):
        """test funkce maximum"""
        assert self.p.maximum([8, -8, 2]) == (8, 1)

    def test_nacteni_soubor(self):
        """test funkce nacteni_souboru"""
        assert self.p.nacteni_soubor("cisla.txt") == [5,5]
        with pytest.raises(FileNotFoundError):
            assert self.p.nacteni_soubor("retra")
        with pytest.raises(ValueError):
            assert self.p.nacteni_soubor("text.txt")

    def test_nacteni_parametr(self):
        """test funkce nacteni_parematru"""
        sys.argv = ["", "5", "4"]
        assert self.p.nacteni_parametr() == [5, 4]
        with pytest.raises(ValueError):
            sys.argv = ["", "nbdvcb", "gfh"]
            self.p.nacteni_parametr()

    def test_generovat(self):
        """test funkce generovat"""
        pole = self.p.generovat()
        assert len(pole) == 20 and all(isinstance(x, (int)) for x in pole)

    def test_pole(self):
        """test funkce pole"""
        sys.argv = ["", "cisla.txt"]
        assert self.p.pole() == [5, 5]
        sys.argv = ["", "5", "4"]
        assert self.p.pole() == [5, 4]
        sys.argv = [""]
        pole = self.p.pole()
        assert len(pole) == 20 and all(isinstance(x, (int)) for x in pole)


    class TestSort:
        """třída pro testování sortů"""
        s = FunkcePole.Sort()

        def test_vyber_sort(self, monkeypatch):
            """test funkce vyber_sortu, za pomocí exit kódů a nastavení inputu"""
            with pytest.raises(SystemExit) as test:
                monkeypatch.setattr('builtins.input', lambda: "b")
                self.s.vyber_sortu([-8, 5, 2])
            assert test.type == SystemExit
            assert test.value.code == "bubble sort zavolan"
            with pytest.raises(SystemExit) as test:
                monkeypatch.setattr('builtins.input', lambda: "s")
                self.s.vyber_sortu([-8, 5, 2])
            assert test.type == SystemExit
            assert test.value.code == "selection sort zavolan"
            with pytest.raises(SystemExit) as test:
                monkeypatch.setattr('builtins.input', lambda: "i")
                self.s.vyber_sortu([-8, 5, 2])
            assert test.type == SystemExit
            assert test.value.code == "insertion sort zavolan"
            with pytest.raises(SystemExit) as test:
                monkeypatch.setattr('builtins.input', lambda: "")
                self.s.vyber_sortu([-8, 5, 2])
            assert test.type == SystemExit
            assert test.value.code == "spatna volba"

        def test_bubble_sort(self):
            """test funkce bubble_sort"""
            assert self.s.bubble_sort([8, -8, 2]) == [-8, 2, 8]

        def test_insertion_sort(self):
            """test funkce insertion_sort"""
            assert self.s.insertion_sort([8, -8, 2]) == [-8, 2, 8]

        def test_selection_sort(self):
            """test funkce selection_sosrt"""
            assert self.s.selection_sort([8, -8, 2]) == [-8, 2, 8]
