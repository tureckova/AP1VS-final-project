from numpy import random
import sys
import os


class FunkcePole:
    def generovat(self):
        pole_nove = []
        for x in range(20):
            pole_nove.append((random.randint(1000)))
        if all(isinstance(x, (int)) for x in pole_nove):
            print("test")
        return pole_nove

    def nacteni_parametr(self):
        try:
            pole_parametr = [int(i) for i in sys.argv[1:]]
        except ValueError:
            raise ValueError("nelze převést na int")
        return pole_parametr

    def nacteni_soubor(self, path):
        if not os.path.isfile(path):
            raise FileNotFoundError("soubor neexistuje")
        with open(path) as f:
                pole_soubor = [int(i) for i in f.read().split(" ") if i.isdigit()]
        if not pole_soubor:
                raise ValueError("nelze převést na int")
        return pole_soubor

    def pole(self):
        if len(sys.argv) == 1:
            pole = self.generovat()
        elif len(sys.argv) == 2:
            pole = self.nacteni_soubor(sys.argv[1])
        else:
            pole = self.nacteni_parametr()
        return pole

    def maximum(self, pole):
        hodnota_max = max(pole)
        return hodnota_max, pole.index(hodnota_max) + 1

    def minimum(self, pole):
        hodnota_min = min(pole)
        return hodnota_min, pole.index(hodnota_min) + 1

    class Sort:

        def vyber_sortu(self, pole):
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
            pole = test_pole
            n = len(pole)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if pole[j] > pole[j + 1]:
                        pole[j], pole[j + 1] = pole[j + 1], pole[j]
            return pole

        def insertion_sort(self, test_pole):
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
