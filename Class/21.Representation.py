print(repr(12e12))

from fractions import Fraction
half = Fraction(1, 2)
"""
>>>repr(half)
'Fraction(1, 2)'
>>>str(half)
'1/2'
>>>print(half)
1/2

eval(repr(object)) == object

s = "Hello, world!"
>>> eval(s)
Error
>>> eval(repr(s))
'Hello, world!'
>>> repr(s)
"'Hello, world!'" 
"""

# f-strings
from math import pi
"""
>>>f'pi starts with {pi}...'
'pi starts with 3.141592653589793...'"""
half.__repr__()

class Ratio:
    def __init__(self,n,d):
        self.numerator = n
        self.denominator = d
    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numerator, self.denominator) # The use of function format
    
    def __str__(self):
        return '{0}/{1}'.format(self.numerator, self.denominator)
    
    def __add__(self, other):
        if isinstance(other, Ratio):
            n = self.numerator * other.denominator + other.numerator * self.denominator
            d = self.denominator * other.denominator
            g = gcd(n, d)
            return Ratio(n // g, d // g)
        elif isinstance(other, int):
            # Convert int to Ratio for addition     
            other = Ratio(other, 1)
            # Now we can use the same logic as above
            return Ratio(self.numerator * other.denominator + other.numerator * self.denominator,
                         self.denominator * other.denominator)
        elif isinstance(other, float):
            # Convert float to Ratio for addition
            return float(self) + other
    __radd__ = __add__

    def __float__(self):
        return self.numerator / self.denominator

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a