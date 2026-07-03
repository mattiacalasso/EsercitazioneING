from math import gcd
import pytest

@pytest.mark.parametrize("integers, expected", [
    ([4, 5], 1),        
    ([3, 7], 1),         
    ([6, 8], 2),          
    ([1, 10], 1),        
    ([12, 15, 20], 1),    
    ([2, 3, 5], 1), 
    ([0,0],0),     
])

def test_gcd(integers, expected):
    assert gcd(*integers) == expected