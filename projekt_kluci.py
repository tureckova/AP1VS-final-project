"""This is out project."""
import string
from collections import Counter


def retezec(retezec):
    """Count frequency of characters.

    ----------
    :param str retezec: Retezec must be string.
    Can include every character in ASCII.
    Příklady funkce:
    ----------
    >>> retezec("banana")
    Tvoje zvolene slovo je: banana
    Tvoje slovo je dlouhe:  6 znaku
    Nejcastejsi znaky jsou
    ('a', 3)
    Nejmene casty znak je: b
    Prumerna cetnost znaku je:  2.0
    Cetnost jednotlivych znaku: Counter({'a': 3, 'n': 2, 'b': 1})
    (6, 'a', 'b', 2.0, Counter({'a': 3, 'n': 2, 'b': 1}))
    >>> retezec(2)
    Traceback (most recent call last):
    ...
    TypeError: Imput must be string.
    >>> retezec("2")
    Tvoje zvolene slovo je: 2
    Tvoje slovo je dlouhe:  1 znaku
    Nejcastejsi znaky jsou
    ('2', 1)
    Nejmene casty znak je: 2
    Prumerna cetnost znaku je:  1.0
    Cetnost jednotlivych znaku: Counter({'2': 1})
    (1, '2', '2', 1.0, Counter({'2': 1}))
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
        """Raises error if input given by user is not string"""
        raise TypeError("Imput must be string.")
    if (retezec == ""):
        """if input is string but has no characters,then the default string"""
        retezec = "banana"
    print("Tvoje zvolene slovo je:", retezec)
    counter = Counter(retezec)
    """variable that stores an amount of each character in string"""
    print("Tvoje slovo je dlouhe: ", len(retezec), "znaku")
    """this line prints the lenght of string"""
    alphabet = string.printable
    dictionary = {}

    for letters in alphabet:
        dictionary[letters] = 0

    for letters in retezec:
        dictionary[letters] += 1
    dictionary = sorted(dictionary.items(),
                        reverse=True,
                        key=lambda x: x[1])
    a = 1
    print("Nejcastejsi znaky jsou")
    for position in range(0, 26):
        print(dictionary[position])
        a += 1
        if position != len(dictionary) - 1:
            if dictionary[position + 1][1] < dictionary[position][1]:
                break
    """variable that stores the most frequent character"""
    countermin = min(counter, key=counter.get)
    print("Nejmene casty znak je:", countermin)
    """variable that stores the least frequent character"""
    countermax = max(counter, key=counter.get)
    sum = 0
    for i in counter:
        """this line sums all integers in counter"""
        sum += counter[i]
    print("Prumerna cetnost znaku je: ", sum/len(counter))
    """this line prints the average frequency of characters"""
    print("Cetnost jednotlivych znaku:", counter)
    """this line prints frequency of each character"""
    maxc = {}
    for i in range(1, a):
        maxc[i] = counter.most_common(i)[0]
    return len(retezec), countermax, countermin, sum/len(counter), counter
