def intToRoman(num):
  
    
    # Storing roman values of digits from 0-9
    # when placed at different places
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
  
    # Převádění na římskou soustavu číslic
    tisice = m[num // 1000]
    sta = c[(num % 1000) // 100]
    desitky = x[(num % 100) // 10]
    jednicky = i[num % 10]
  
    vysledek = (tisice + sta + desitky + jednicky)

    return vysledek

# Testovací kód
def main():
    print("Zadej cislo, ktere chces prevest do Rimske soustavy: ")
    # Vstupní kód uživatele
    number = int(input())
    # Výstupní číslo v římské soustavě
    print(intToRoman(number))

if __name__ == "__main__":
    main()