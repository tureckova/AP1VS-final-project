"""Program na zjištění a vypsání četnosti znaků."""

import unidecode
from collections import Counter


def get_file_choice():
    """
    Tato funkce ukládá input ze souboru zadán uživatelem.

    Výstupní hodnota:
    :return input_text: String ve kterém je uložen input.

    >>> get_file_choice()
    test_text
    """
    print("\nZadejte název souboru i s připonou\nPříklad: readme.txt"
          "\nSoubor musí být ve stejné složce jako program")
    file_path = input("->")
    with open(file_path, "r") as f:
        input_text = f.read()
    return input_text


def get_user_input():
    """
    Tato funkce ukládá uživatelský input zadáván ručně.

    Výstupní hodnota:
    :return input_text: String ve kterém je uložen input.

    >>> get_user_input()
    test_text
    """
    print("\nZde můžete začít psát svůj parametr"
          "\nNemusíte se bát zmáčknout enter - program vám dovolí psát,"
          "dokud nepoužijete znak # samostatně")
    input_text = ""
    input_char = input("->")
    while input_char != '#':
        input_text += input_char
        input_char = input("->")
    return input_text


def choices(choice):
    """
    Tato funkce měří počet znaků obsažených ve stringu.

    Parametry:
    :param choice: String ve kterém je uložena možnost.

    Výstupní hodnota:
    :return input_text: String ve kterém je uložen input.

    >>> choices("1")
    test_text

    >>> choices("2")
    test_text
    """
    if choice == "1":
        return get_file_choice()
    if choice == "2":
        return get_user_input()


def cleared_text(input_text):
    """
    Funkce pro upravení textu.

    Tato funkce bere string jako input (input_text) a vrací jeho
    upravenou verzi bez diakritiky, mezer a všech písmen
    převedených na malá písmena.

    Parametry:
    :param input_text: String, který má být upraven.

    Výstupní hodnota:
    :return clean: String, který je již upravený.

    >>> cleared_text("Ahoj jak se máš")
    'ahojjaksemas'
    >>> cleared_text("12 Opic se směje")
    '12opicsesmeje'
    """
    input_text = unidecode.unidecode(input_text)
    input_text = input_text.lower()
    input_text = input_text.replace(" ", "")
    clean = input_text
    return clean


def all_letters(clean):
    """
    Tato funkce měří počet znaků obsažených ve stringu.

    Parametry:
    :param clean: String ze kterého se budou počítat znaky.

    Výstupní hodnota:
    :return celkovy_pocet: Počet (Int) znaků obsažených ve stringu.

    >>> all_letters("ahoj24ja//jsem..jarda")
    21
    """
    celkovy_pocet = len(cleared_text(clean))
    return celkovy_pocet


def most_frequent_letter(clean):
    """
    Tato funkce zjišťuje nejvíce užitý znak ve stringu.

    Parametry:
    :param clean: String ze kterého bude znak zjišťován.

    Výstupní hodnota:
    :return most_frequent: Vrací znak (char) a jeho počet (int).

    >>> most_frequent_letter("21242526ztbv22257///lps")
    ('2', 7)
    """
    counter = Counter(cleared_text(clean))
    most_frequent = counter.most_common(1)[0]
    return most_frequent


def least_frequent_letter(clean):
    """
    Tato funkce zjišťuje nejméně užitý znak ve stringu.

    Parametry:
    :param clean: String ze kterého bude znak zjišťován.

    Výstupní hodnota:
    :return least_frequent: Vrací znak (char) a jeho počet (int).

    >>> least_frequent_letter("aaa2222////b3333....wwww")
    ('b', 1)
    """
    counter = Counter(cleared_text(clean))
    least_frequent = counter.most_common()[-1]
    return least_frequent


def average_letter_frequency(clean):
    """
    Tato funkce počítá průměrnou četnost znaků.

    Parametry:
    :param clean: String, ze kterého je průměr počítán.

    Výstupní hodnota:
    :return average_frequency: Vypíše průměrnou četnost všech znaků.

    >>> average_letter_frequency("whjgjk51448/(!':!'bhjshf547453")
    0.4
    """
    total_letters = 0
    for char in clean:
        if char.isalpha():
            total_letters += 1
    average_frequency = total_letters/len(clean)
    return average_frequency


def appereance_of_every_letter(clean):
    """
    Tato funkce zjišťuje, kolikrát se každé písmeno objevuje ve stringu.

    Parametry:
    :param clean: String, ze kterého jsou písmena přebírána.

    Výstup:
    Vypíše počet výskytů každého písmene abecedy.

    >>> appereance_of_every_letter("aaaabbbccd")
    <BLANKLINE>
    Kolikrát byl který znak použit podle abecedy
    a : 4
    b : 3
    c : 2
    d : 1
    e : 0
    f : 0
    g : 0
    h : 0
    i : 0
    j : 0
    k : 0
    l : 0
    m : 0
    n : 0
    o : 0
    p : 0
    q : 0
    r : 0
    s : 0
    t : 0
    u : 0
    v : 0
    w : 0
    x : 0
    y : 0
    z : 0
    {'a': 4, 'b': 3, 'c': 2, 'd': 1}
    """
    alphabet_count = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print("\nKolikrát byl který znak použit podle abecedy")

    for char in clean:
        if char in alphabet:
            if char in alphabet_count:
                alphabet_count[char] += 1
            else:
                alphabet_count[char] = 1
    for char in alphabet:
        if char in alphabet_count:
            print(char + ' : ' + str(alphabet_count[char]))
        else:
            print(char + ' : 0')
    return alphabet_count


if __name__ == '__main__':
    while True:
        print("\nZvolte si možnost vstupu"
              "\n1 -> vstup ze souboru"
              "\n2 -> zadání vstupu ručně")
        choice = input("\nZde zadejte vaši možnost ->")
        if (choice == "1" or choice == "2"):
            break

    text = choices(choice)

    print("\nCelkový počet znaků je ", all_letters(text))
    print("\nNejvíce použitý znak je ", most_frequent_letter(text))
    print("\nNejméně použitý znak je ", least_frequent_letter(text))
    print("\nPrůměrná četnost znaků je ", average_letter_frequency(text))
    appereance_of_every_letter(text)
