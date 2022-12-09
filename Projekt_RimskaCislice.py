"""Prevod arabskych cisel na rimske.

Vypracovali: Do, Janostik, Lunga, Blaho
"""


"""Seznam zakladni rimskych cisel.
I	V	X	L	C	D	M
1	5	10	50	100	500	1000
"""


def kontrola(cislo):
    """Kontrola zda je mozne cislo prevodit.

    Parameters
    ----------
    cislo : int
    """
    # Lze prevadet cisla od 1 do 3999
    if isinstance(cislo, str) or isinstance(cislo, float):
        raise TypeError("Nelze prevodit")
    elif cislo > 3999:
        print("Nelze prevodit. Cislo je vetsi nez 3999")
    elif cislo == 0:
        print("Nelze prevodit. RimskÃ© cislice neobsahuji symbol pro nulu")
    elif cislo < 0:
        print("Nelze prevodit. Rismke cislice nelze napsat v zapornych cisel")
    else:
        main()


def tisice(cislo):
    """Zjisteni tisice.

    Funkce vypocita zadane cislo a ulozi znak na dane pozici.

    Parameters
    ----------
    cislo: int

    Returns
    -------
    tisice_output: string

    Examples
    --------
    >>> tisice(3888)
    'MMM'

    """
    t = ["", "M", "MM", "MMM"]  # index v poli zacina s hodnotou 0
    if isinstance(cislo, str) or isinstance(cislo, float):
        raise TypeError("Nelze prevodit")
    tisic = t[cislo // 1000]  # 3888 // 1000 == 3
    return tisic  # znak na (3+1) pozici


def stovky(cislo):
    """Zjisteni stovky.

    Funkce vypocita zadane cislo a ulozi znak na dane pozici.

    Parameters
    ----------
    cislo: int

    Returns
    -------
    stovky_output: string

    Examples
    --------
    >>> stovky(3888)
    'DCCC'

    """
    # index v poli zacina s hodnotou 0
    s = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    if isinstance(cislo, str) or isinstance(cislo, float):
        raise TypeError("Nelze prevodit")
    sto = s[(cislo % 1000) // 100]  # (3888 % 1000) // 100 == 8
    return sto  # znak na (8+1) pozici == DCCC


def desitky(cislo):
    """Zjisteni desitky.

    Funkce vypocita zadane cislo a ulozi znak na dane pozici.

    Parameters
    ----------
    cislo: int

    Returns
    -------
    desitky_output: string

    Examples
    --------
    >>> desitky(3888)
    'LXXX'

    """
    # index v poli zacina s hodnotou 0
    d = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    if isinstance(cislo, str) or isinstance(cislo, float):
        raise TypeError("Nelze prevodit")
    deset = d[(cislo % 100) // 10]  # (3888 % 100) // 10 == 8
    return deset  # znak na (8+1) pozici == LXXX


def jednotky(cislo):
    """Zjisteni desitky.

    Funkce vypocita zadane cislo a ulozi znak na dane pozici.

    Parameters
    ----------
    cislo: int

    Returns
    -------
    jednotky_output: string

    Examples
    --------
    >>> jednotky(3888)
    'XIII'

    """
    # index v poli zacina s hodnotou 0
    j = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    if isinstance(cislo, str) or isinstance(cislo, float):
        raise TypeError("Nelze prevodit")
    jednotka = j[cislo % 10]  # 3888 % 10 == 8
    return jednotka  # znak na (8+1) pozici == VIII


def vysledek():
    """Sjednoceni znaku."""
    vysledek = tisice(cislo) + stovky(cislo) + desitky(cislo) + jednotky(cislo)
    return vysledek  # MMM + DCCC + LXXX + VIII


def main():
    """Vysledek."""
    print("Prevod na rimsky: " + vysledek())


if __name__ == "__main__":
    print("\nRismke cislice lze prevadet pouze prirozena cisla od 1 do 3999")
    while True:
        try:
            cislo = int(input("\nZadejte cislo na prevod: "))
            kontrola(cislo)
        except ValueError:
            print("Nelze prevodit. Zadali jste spatny vstup\n")

    while True:
        znova = str(input("\nSpustit znovu? (y/n): "))
        if znova in ('y', 'n'):
            break
        print("Neplatny vstup.")
        if znova == 'y':
            continue
        else:
            print("Ukoncuji program.")
            break
         
