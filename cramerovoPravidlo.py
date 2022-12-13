"""Program na vypocet sustavy linearnych rovnic pomocou Cramerovho pravidla."""


print("zadej matici po jednotlivych radcich vcetne pravych stran ")
print("jednotliva data jsou oddelena carkami ")

'''
Zadanie hodnot neznamych.

:param a1: Vstpny parameter a1
:param a2: Vstupny parameter a2
:param a3: Vstupny parameter a3
'''

a1 = input("zadej prvni radek")
a2 = input("zadej druhy radek")
a3 = input("zadej treti radek")

'''
Split riadkov na indexy po ",".
'''

ay1 = str.split(a1, ",")
ay2 = str.split(a2, ",")
ay3 = str.split(a3, ",")

'''
Prevod na realne cislo.
'''

a11 = float(ay1[0])
a12 = float(ay1[1])
a13 = float(ay1[2])
b1 = float(ay1[3])
a21 = float(ay2[0])
a22 = float(ay2[1])
a23 = float(ay2[2])
b2 = float(ay2[3])
a31 = float(ay3[0])
a32 = float(ay3[1])
a33 = float(ay3[2])
b3 = float(ay3[3])

'''
Funkcia na vypocet determinantu.
'''


def determinant(a11, a21, a31, a12, a22, a32, a13, a23, a33):
    """Funkcia na vypocet determinantu."""
    a = a11*a22*a33+a12*a23*a31+a13*a21*a32-a13*a22*a31-a12*a21*a33
    a = a-a11*a23*a32
    return (a)


'''
Volanie funkcie
'''

deta = determinant(a11, a21, a31, a12, a22, a32, a13, a23, a33)
deta1 = determinant(b1, b2, b3, a12, a22, a32, a13, a23, a33)
deta2 = determinant(a11, a21, a31, b1, b2, b3, a13, a23, a33)
deta3 = determinant(a11, a21, a31, a12, a22, a32, b1, b2, b3)

'''
Vypocet  x,y,z.
'''

x = deta1/deta
y = deta2/deta
z = deta3/deta

'''
Print vysledku.
'''

print("vysledek x= ", x, "y= ", y, "z=", z)
print("konec programu")
