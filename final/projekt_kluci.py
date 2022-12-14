"""Program na počítání jednotlivých symbolů ve stringu."""
from collections import Counter


def retezec(retezec):
    """Function that returns informations about given string"""
    """příklady Funkce.

    Sample usage:
    >>>retezec("blablalbalba")
    Tvoje zvolene slovo je: blablalbalba
    Tvoje slovo je dlouhe:  12 znaku
    CeTnost jednotlivych znaku je rovna
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
        """Raises error if input given by user is not string"""
        raise TypeError("Imput must be string.")
    if (retezec == ""):
        """if input is string but has no characters,then the default string is banana"""
        retezec = "banana"
    print("Tvoje zvolene slovo je:", retezec)
    counter = Counter(retezec)
    """variable that stores an amount of each character in string"""
    print("Tvoje slovo je dlouhe: ", len(retezec), "znaku")
    """this line prints the lenght of string"""
    countermax = max(counter, key=counter.get)
    """variable that stores the most frequent character"""
    countermin = min(counter, key=counter.get)
    """variable that stores the least frequent character"""
    if (countermax != countermin):
        """if variables countermax and countermin are different, then it do this ↓"""
        print("Nejcastejsi znak je:", countermax)
        """this line prints most frequent character"""
        print("Nejmene casty znak je:", countermin)
        """this line prints least frequent character"""
        else:
        """if variables countermax and countermin are equal, then it do this ↓"""
        print("CeTnost jednotlivych znaku je rovna")
    sum = 0
    for i in counter:
        """this line sums all integers in counter"""
        sum += counter[i]
    print("Prumerna cetnost znaku je: ", sum/len(counter))
    """this line prints the average frequency of characters"""
    print("Cetnost jednotlivych znaku:", counter)
    """this line prints frequency of each character"""
    return len(retezec), countermax, countermin, sum/len(counter), counter

