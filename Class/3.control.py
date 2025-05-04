
from math import pi,sin,sqrt
def is_prime(n):
    """
    >>>is_prime(7)
    True
    >>>is_prime(9)
    False
    >>>is_prime(797)
    True
    exit"""
    i=2
    while i<=int(sqrt(n)):
        if n%i==0:
            return False
        i=i+1
    return True


 #Homework 1:
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    k=n-1
    while k>=1:
        if n%k==0:
            return k
        k=k-1
        
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    step=1
    if n==1:
        print(1)
        return 1
    while n>1:
        print(n)
        if n%2==0:
         n=n//2
        else :n=n*3+1
        step+=1
    print(1)
    return step    
