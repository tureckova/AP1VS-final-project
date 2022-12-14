"""
Program na počítání jednotlivých symbolů ve stringu
"""
from collections import Counter

def retezec(retezec):
    """Funkce

    Sample usage:
    >>>retezec("blablalbalba")
    Tvoje zvolene slovo je: blablalbalba
    Tvoje slovo je dlouhe:  12 znaku
    Nejcastejsi znak je: b
    Nejmene casty znak je: b
    Prumerna cetnost znaku je:  4.0
    Cetnost jednotlivych znaku: Counter({'b': 4, 'l': 4, 'a': 4})
    >>>retezec(2)
    Traceback (most recent call last):
    ...
    TypeError: Imput must be string.
    >>> retezec("2")
    Tvoje zvolene slovo je: 2
    Tvoje slovo je dlouhe:  1 znaku
    Nejcastejsi znak je: 2
    Nejmene casty znak je: 2
    Prumerna cetnost znaku je:  1.0
    Cetnost jednotlivych znaku: Counter({'2': 1})
    >>> retezec()
    Traceback (most recent call last):
    ...
    TypeError: retezec() missing 1 required positional argument: 'retezec'
    >>> retezec(False)
    Traceback (most recent call last):
    ...
    TypeError: Imput must be string.
    """
    if type(retezec) not in [str]:
            raise TypeError("Imput must be string.")
    if (retezec == ""):
        retezec = "banana"
    print("Tvoje zvolene slovo je:", retezec)
    counter = Counter(retezec)
    print("Tvoje slovo je dlouhe: ", len(retezec), "znaku")
    countermax = max(counter, key=counter.get)
    print("Nejcastejsi znak je:", countermax)
    countermin = min(counter, key=counter.get)
    print("Nejmene casty znak je:", countermin)
    sum = 0
    for i in counter:
        sum += counter[i]
    print("Prumerna cetnost znaku je: ", sum/len(counter))
    print("Cetnost jednotlivych znaku:", counter)
    return len(retezec),countermax,countermin,sum/len(counter),counter
