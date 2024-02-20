import pytest
import utils

def test_fact():
    # À compléter...
    assert utils.fact(7) == 5040

def test_roots():
    
    assert utils.root(4,3,6) == 4 

def test_integrate():
    # À compléter...  
    assert utils.integrate( "x^2" , 3, 7) == 7