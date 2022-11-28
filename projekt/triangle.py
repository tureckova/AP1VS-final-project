'''
@mainpage
@brief This is a simple example of documentation generated via Doxygen.
@section Triangle calculator
@author Filip Hajduch, Libor Výleta
@version 1.0
@brief
This program is calculating triangle from points.

 -*- coding: UTF-8 -*-
 '''
import math


def triangle(x1, y1, x2, y2, x3, y3):

    if type(x1) not in [int, float] or type(x2) not in [int, float] \
            or type(x3) not in [int, float] or type(y1) not in [int, float] \
            or type(y2) not in [int, float] or type(y3) not in [int, float]:
        raise TypeError()

    else:

        # vypocet strany a
        a1 = x2 - x1
        b1 = y2 - y1
        a = math.sqrt(math.pow(a1, 2) + math.pow(b1, 2))

        # vypocet strany b
        a2 = x3 - x2
        b2 = y3 - y2
        b = math.sqrt(math.pow(a2, 2) + math.pow(b2, 2))

        # vypocet strany c
        a3 = x3 - x1
        b3 = y3 - y1
        c = math.sqrt(math.pow(a3, 2) + math.pow(b3, 2))

        # podminka jestli jde trojuhelnik sestavit
        if a+b > c or a+c > b or b+c > a:
            # vypocet obsahu pres heronuv vzorec
            s = (a + b + c) / 2
            obsah = math.sqrt(s * (s - a) * (s - b) * (s - c))

            print("Trojuhelnik lze sestavit")
            print("Delka strany a: ", a)
            print("Delka strany b: ", b)
            print("Delka strany c: ", c)
            print("Obsah :", obsah)
            print("Obvod:", round(a + b + c, 2))

            # vypocet uhlu alfa
            alfa1 = (math.pow(b, 2) + math.pow(c, 2) - math.pow(a, 2)) / \
                    (2 * b * c)
            alfa = math.acos(alfa1)

            # vypocet uhlu beta
            beta1 = (math.pow(a, 2) + math.pow(c, 2) - math.pow(b, 2)) / \
                    (2 * a * c)
            beta = math.acos(beta1)

            # vypocet uhlu gama
            gama1 = (math.pow(a, 2) + math.pow(b, 2) - math.pow(c, 2)) / \
                    (2 * a * b)
            gama = math.acos(gama1)

            # podminka jestli je trojuhelnik pravouhly
            if round(math.degrees(alfa), 2) == 90 \
                    or round(math.degrees(beta), 2) == 90 \
                    or round(math.degrees(gama), 2) == 90:
                print("Trojuhelnik je pravouhly")
            else:
                print("Trojuhelnik neni pravouhly")

            print("Uhel alfa = ", round(math.degrees(alfa), 2))
            print("Uhel beta = ", round(math.degrees(beta), 2))
            print("Uhel gama = ", round(math.degrees(gama), 2))

        else:
            print("Trojuhelnik nelze sestavit")
