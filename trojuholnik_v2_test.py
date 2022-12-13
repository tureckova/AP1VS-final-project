import pytest
from trojuholnik_v2 import *

def test_obvodu():
    assert obvod_Stran(2,2,2)== 6.0
    
def test_Obsah():
    assert Obsah_Trojuholnika(5,5,8)==12.0
    
def test_Strana():
    assert strana(1,2,2,1)==(((1-2)**2+(2-1)**2)**(1/2))
        
def test_Uhol():
    assert uhol(0,1,1,0,0,0)==90.00000000000001