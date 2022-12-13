"""this program is counting characters in string."""
from collections import Counter
x = True
while x is True:
    retezec = input("Zadejte retezec: ")
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
    continu = input("Pro pokracovani napiste dalsi: ")
    if continu == "dalsi":
        x = True
    else:
        x = False
