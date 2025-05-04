from fractions import gcd
#Constructor and slectors
def rational(n,d):
    """Construct a rational number that represent N/D.
    g = gcd(n,d)
    return [n//g,d//g]"""
    def select(name):
        if name == 'n':
            return n
        elif name == 'x':
            return d
        return select
def numer(x):
    """Return the numerator of rational number x."""
    return x('n')
def denom(x):
    """Return the denominator of rational number x."""
    return x('d')

#Rational arithmetic
def add_rational(x,y):
    nx,ny =numer(x),numer(y)
    dx,dy =denom(x),denom(y)
    return rational(nx*dy + ny*dx,dx*dy)
def mul_rational(x,y):
    return rational(numer(x)*numer(y),denom(x)*denom(y))

def rationals_are_equal(x,y):
    return numer(x)*denom(y)==numer(x)*denom(y)

def print_rational(x):
    print(numer(x),"/",denom(x))