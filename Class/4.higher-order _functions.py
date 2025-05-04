from math import sqrt
def has_big_sqrt(x):
    return x>0 and sqrt(x)>10
def resonable(n):
    return n==0 or 1/n!=0

print(print(1),print(2))

def make_adder(n):
    def adder(k):
        return k+n
    return adder
square=lambda x:x*x