"""Soubor obsahuje funkce pouzivane v mainu."""
from numpy import random
import sys
import os


class FunkcePole:
    """Obsahuje funkce potrebne pro prace s poli v projektu."""

    def generovat(self):
        """
        Generuje nahodne pole.

            Args:
                pole_nove: prazdne pole
                x: pozice v poli
            Returns:
                pole_nove: pole naplnene nahodnymi cisly
        """
        pole_nove = []
        for x in range(20):
            pole_nove.append((random.randint(1000)))
        return pole_nove

    def nacteni_parametr(self):
        """
        Nacita pole z parametru.

            Args:
                pole_parametr: pole nacte parametry spusteni
            Returns:
                pole_parametr: pole obsahujici parametry
        """
        pole_parametr = [int(i) for i in sys.argv[1:]]
        if pole_parametr == []:
            raise ValueError("nelze převést na int")
        return pole_parametr

    def nacteni_soubor(self, path):
        """
        Nacita pole ze souboru.

            Param:
                path: cesta k souboru obsahujici pole
            Args:
                pole_soubor: pole nacte cisla ze souboru
            Returns:
                pole_soubor: pole s cisly ze souboru
        """
        if not os.path.isfile(path):
            raise FileNotFoundError("soubor neexistuje")
        with open(path) as f:
            pole_soubor = [int(i) for i in f.read().split(" ") if i.isdigit()]
        if pole_soubor == []:
            raise ValueError("nelze převést na int")
        return pole_soubor

    def pole(self):
        """
        Urcuje typ vytvoreni pole dle nactenych parametru.

            Args:
                pole: vytvori pole pomoci funkci dle zvolenych parametru
            Returns:
                pole: pole s cisly
        """
        if len(sys.argv) == 1:
            pole = self.generovat()
        elif len(sys.argv) == 2:
            pole = self.nacteni_soubor(sys.argv[1])
        else:
            pole = self.nacteni_parametr()
        return pole

    def maximum(self, pole):
        """
        Urcuje nejvyssi cislo v poli a jeho pozici.

            Param:
                pole: pole s cisly z funkce pole()
            Args:
                hodnota_max: nejvyssi cislo v poli
            Returns:
                hodnota_max: nejvyssi cislo v poli
                pole.index(hodnota_max)+1: pozice nejvyssiho cisla v poli
        """
        hodnota_max = max(pole)
        return hodnota_max, pole.index(hodnota_max) + 1

    def minimum(self, pole):
        """
        Urcuje nejvyssi cislo v poli a jeho pozici.

            Param:
                pole: pole s cisly z funkce pole()
            Args:
                hodnota_min: nejnizsi cislo v poli
            Returns:
                hodnota_min: nejnizsi cislo v poli
                pole.index(hodnota_min)+1: pozice nejnizsiho cisla v poli
        """
        hodnota_min = min(pole)
        return hodnota_min, pole.index(hodnota_min) + 1

    class Sort:
        """Obsahuje funkce potrebne pro serazeni poli."""

        def vyber_sortu(self, pole):
            """
            Vybira typ sortu na zaklade vyberu.

                Param:
                    pole: pole s cisly z funkce pole()
                Args:
                    x: znak pro vyber sortu
            """
            print(".....\n"
                  "Vyberte si serazovaci algoritmus:\n"
                  "b = bubbleSort\n"
                  "i = insertionSort\n"
                  "s = selectionSort\n"
                  ".....")
            x = input()
            if x == "b":
                self.bubble_sort(pole)
                print(pole)
                sys.exit("bubble sort zavolan")
            elif x == "i":
                self.insertion_sort(pole)
                print(pole)
                sys.exit("insertion sort zavolan")
            elif x == "s":
                self.selection_sort(pole)
                print(pole)
                sys.exit("selection sort zavolan")
            else:
                print("spatna volba")
                sys.exit("spatna volba")

        def bubble_sort(self, test_pole):
            """
            Serazuje pole od nejmensiho po nejvetsi.

                Param:
                    test_pole: pole s cisly z funkce pole()
                Args:
                    pole: pole s cisly z test_pole
                    n: delka pole
                    i: cislo v poli
                    j: cislo v poli
                Returns:
                    pole: serazene pole od nejmensiho po nejvetsi
            """
            pole = test_pole
            n = len(pole)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if pole[j] > pole[j + 1]:
                        pole[j], pole[j + 1] = pole[j + 1], pole[j]
            return pole

        def insertion_sort(self, test_pole):
            """
            Serazuje pole od nejmensiho po nejvetsi.

                Param:
                    test_pole: pole s cisly z funkce pole()
                Args:
                    pole: pole s cisly z test_pole
                    cislo: cislo v poli
                    i: pozice cisla v poli
                    j: pozice cisla v poli
                Returns:
                    pole: serazene pole od nejmensiho po nejvetsi
            """
            pole = test_pole
            for i in range(1, len(pole)):
                cislo = pole[i]
                j = i - 1
                while j >= 0 and cislo < pole[j]:
                    pole[j + 1] = pole[j]
                    j -= 1
                pole[j + 1] = cislo
            return pole

        def selection_sort(self, test_pole):
            """
            Serazuje pole od nejmensiho po nejvetsi.

                Param:
                    test_pole: pole s cisly z funkce pole()
                Args:
                    pole: pole s cisly z test_pole
                    p: docasna pozice cisla v poli
                    mini: aktualni nejmensi cislo v poli?
                    i: pozice cisla v poli
                    j: pozice cisla v poli
                Returns:
                    pole: serazene pole od nejmensiho po nejvetsi
            """
            pole = test_pole
            for i in range(0, len(pole) - 1):
                p = 0
                mini = pole[-1]
                for j in range(i, len(pole)):
                    if pole[j] <= mini:
                        mini = pole[j]
                        p = j
                pole[i], pole[p] = pole[p], pole[i]
            return pole
