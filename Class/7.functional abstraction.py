def curry(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g


a=1
def f(g):
    a=2
    return lambda y: a*g(y)
f(lambda y:a+y)(a)

def trace(f):
    def traced(n):
        result=f(n)
        print('called',f,'on',n,'and got',result)
        return result
    return traced
@trace
def square(x):
    return x*x

def sum_of_squares(n):
    i=1
    total=0
    while i<=n:
        total=total+square(i)
        i=i+1
    return total

def search(f):
    x=0
    while not f(x):
        x=x+1
    return x
def inverse(f):
    "Return a function g(y) that returns x such that f(x)==y. "
    return lambda y: search(lambda x:f(x)==y)

sqrt=inverse(square)
        

