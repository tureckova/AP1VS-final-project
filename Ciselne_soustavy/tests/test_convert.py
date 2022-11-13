from sys import path
path.append("C:/Users/marti/Plocha/FAI UTB/První ročník/Zimní Semestr/Nástroje pro vývoj softwarových projektů/Projekt/AP1VS-final-project/Číselné_soustavy/")
from kód import Ciselne_soustavy

def test_to_digits():
    assert Ciselne_soustavy.to_digits(5) == [5]
    assert Ciselne_soustavy.to_digits(12) == [1, 2]
    assert Ciselne_soustavy.to_digits(390) == [3, 9, 0]
    assert Ciselne_soustavy.to_digits(6541) == [6, 5, 4, 1]
    assert Ciselne_soustavy.to_digits(515625) == [5, 1, 5, 6, 2, 5]
    assert Ciselne_soustavy.to_digits(17263527183414) == [
        1, 7, 2, 6, 3, 5, 2, 7, 1, 8, 3, 4, 1, 4] 


def test_to_decimal():
    assert Ciselne_soustavy.to_decimal(2, 10, []) == 2
    assert Ciselne_soustavy.to_decimal(16, 20, []) == 32
    assert Ciselne_soustavy.to_decimal(8, 47, []) == 39
    assert Ciselne_soustavy.to_decimal(2, 111100, []) == 60
    assert Ciselne_soustavy.to_decimal(14, 154, []) == 270
    assert Ciselne_soustavy.to_decimal(20, 134, []) == 464
    assert Ciselne_soustavy.to_decimal(17, 1198, []) == 5363

def test_to_dest_base():
    assert Ciselne_soustavy.to_destination_base(2, 12) == ["1", "1", "0", "0"]
    assert Ciselne_soustavy.to_destination_base(16, 58) == ["3", "A"]
    assert Ciselne_soustavy.to_destination_base(8, 5830) == ["1", "3", "3", "0", "6"]
    assert Ciselne_soustavy.to_destination_base(2, 78) == ["1", "0", "0", "1", "1", "1", "0"]
    assert Ciselne_soustavy.to_destination_base(8, 78) == ["1", "1", "6"]
    assert Ciselne_soustavy.to_destination_base(16, 78) == ["4", "E"]



def test_convert():
    assert Ciselne_soustavy.convert(10, 1, "6") == "111111"
    assert Ciselne_soustavy.convert(2, 16, "11011") == "1B"
    assert Ciselne_soustavy.convert(8, 10, "65") == "53"
    assert Ciselne_soustavy.convert(10, 36, "1000") == "RS"
    assert Ciselne_soustavy.convert(10, 16, "7899") == "1EDB"
    assert Ciselne_soustavy.convert(16, 2, "69CB") == "110100111001011"


