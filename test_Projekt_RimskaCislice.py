"""Import from Projekt_RimskaCislice."""
# Vypracoval M. Blaho
from Projekt_RimskaCislice import tisice
from Projekt_RimskaCislice import stovky
from Projekt_RimskaCislice import desitky
from Projekt_RimskaCislice import jednotky
from Projekt_RimskaCislice import kontrola
import pytest


def test_tisice():
    """Testovanie."""
    # cisla z intervalu 0-999
    assert tisice(0) == ''
    assert tisice(999) == ''

    # cislo 2000 - 2999
    assert tisice(1000) == 'M'
    assert tisice(1999) == 'M'

    # cislo 2000 - 2999
    assert tisice(2000) == 'MM'
    assert tisice(2999) == 'MM'

    # cisla z intervalu 3000 - 3999
    assert tisice(3000) == 'MMM'
    assert tisice(3999) == 'MMM'

    # cislo nie je int
    with pytest.raises(TypeError):
        tisice("Nemozno prevodit")

    # cislo je viac ako
    with pytest.raises(IndexError):
        tisice(4000)


def test_stovky():
    """Testovanie."""
    # cisla z intervalu 0-99
    assert stovky(0) == ''
    assert stovky(99) == ''

    # cisla z intervalu 100 - 199
    assert stovky(100) == 'C'
    assert stovky(199) == 'C'

    # cisla z intervalu 200 - 299
    assert stovky(200) == 'CC'
    assert stovky(299) == 'CC'

    # cisla z intervalu 300 - 399
    assert stovky(300) == 'CCC'
    assert stovky(399) == 'CCC'

    # cisla z intervalu 400 - 499
    assert stovky(400) == 'CD'
    assert stovky(499) == 'CD'

    # cisla z intervalu 500 - 599
    assert stovky(500) == 'D'
    assert stovky(599) == 'D'

    # cisla z intervalu 600 - 699
    assert stovky(600) == 'DC'
    assert stovky(699) == 'DC'

    # cisla z intervalu 700 - 799
    assert stovky(700) == 'DCC'
    assert stovky(799) == 'DCC'

    # cisla z intervalu 800 - 899
    assert stovky(800) == 'DCCC'
    assert stovky(899) == 'DCCC'

    # cisla z intervalu 900 - 999
    assert stovky(900) == 'CM'
    assert stovky(999) == 'CM'

    # cislo nie je int
    with pytest.raises(TypeError):
        stovky("Nemozno prevodit")


def test_desitky():
    """Testovanie."""
    # cisla z intervalu 0-9
    assert desitky(0) == ''
    assert desitky(9) == ''

    # cisla z intervalu 10 - 19
    assert desitky(10) == 'X'
    assert desitky(19) == 'X'

    # cisla z intervalu 20 - 29
    assert desitky(20) == 'XX'
    assert desitky(29) == 'XX'

    # cisla z intervalu 30 - 39
    assert desitky(30) == 'XXX'
    assert desitky(39) == 'XXX'

    # cisla z intervalu 40 - 49
    assert desitky(40) == 'XL'
    assert desitky(49) == 'XL'

    # cisla z intervalu 50 - 59
    assert desitky(50) == 'L'
    assert desitky(59) == 'L'

    # cisla z intervalu 60 - 69
    assert desitky(60) == 'LX'
    assert desitky(69) == 'LX'

    # cisla z intervalu 70 - 79
    assert desitky(70) == 'LXX'
    assert desitky(79) == 'LXX'

    # cisla z intervalu 80 - 89
    assert desitky(80) == 'LXXX'
    assert desitky(89) == 'LXXX'

    # cisla z intervalu 90 - 99
    assert desitky(90) == 'XC'
    assert desitky(99) == 'XC'

    # cislo nie je int
    with pytest.raises(TypeError):
        stovky("Nemozno prevodit")


def test_jednotky():
    """Testovanie."""
    # cislo == 0
    assert jednotky(0) == ''

    # cislo == 1
    assert jednotky(1) == 'I'

    # cislo == 2
    assert jednotky(2) == 'II'

    # cislo == 3
    assert jednotky(3) == 'III'

    # cislo == 4
    assert jednotky(4) == 'IV'

    # cislo == 5
    assert jednotky(5) == 'V'

    # cislo == 6
    assert jednotky(6) == 'VI'

    # cislo == 7
    assert jednotky(7) == 'VII'

    # cislo == 8
    assert jednotky(8) == 'VIII'

    # cislo == 9
    assert jednotky(9) == 'IX'

    # cislo nie je int
    with pytest.raises(TypeError):
        stovky("Nemozno prevodit")


def test_kontorla():
    """Testovanie."""
    assert kontrola(4000) == print("Nemozno prevodit")
    assert kontrola(0) == print("Nemozno prevodit")
    assert kontrola(-1) == print("Nemozno prevodit")

    with pytest.raises(TypeError):
        kontrola("Nemozno prevodit")
