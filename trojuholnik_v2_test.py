import pytest
from trojuholnik_v2 import *

"""Vytvorenie funkcie pre testovanie obvodu"""
def test_obvodu():
    """Porovnanie obvodu, že ci hodi spravnu hodnotu"""
    assert obvod_Stran(2,2,2)== 6.0
    
"""Vytvorenie funkcie pre testovanie obsahu""" 
def test_Obsah():
    """Porovnanie obsahu, že ci hodi spravnu hodnotu"""
    assert Obsah_Trojuholnika(5,5,8)==12.0

"""Vytvorenie funkcie pre testovanie Strany"""     
def test_Strana():
    """Porovnanie nami definovanu funkciu na vypocet strany a vysledku"""
    assert strana(1,2,2,1)==(((1-2)**2+(2-1)**2)**(1/2))

"""Vytvorenie funkcie pre testovanie Uhlu"""             
def test_Uhol():
    """Porovnanie nami definovanej funkcie na vypocet uhlov a vysledku"""
    assert uhol(0,1,1,0,0,0)==90.00000000000001