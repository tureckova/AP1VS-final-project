import pytest
from trojuholnik_v2 import *

def test_obvodu():
    assert obvod_Stran(2,2,2)== 6
    
def test_Obsah():
    assert Obsah_Trojuholnika(2,2,2)==1,732050807568877
    
def test_Strana():
    assert strana(1,2,2,1)==1,414213562373095

