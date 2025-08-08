# raise
def double(x):
    if isinstance(x, str):
        raise TypeError('double takes only numbers')
    return 2*x

#Try Statements
try:
    x = 1/0
except ZeroDivisionError as e:
    print('handling a', type(e))
    x = 0

def reduce(f, s, initial):
    for x in s:
        initial = f(initial, x)
    return initial 

from operator import truediv

def divide_all(n, ds):
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')
    

class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest  = rest

nil = ()   # or however you represent the empty list

#dis09-25Summer Q6
def print_evals(expr):
        """Print the expressions that are evaluated while evaluating expr.

        expr: a Scheme expression containing only (, ), +, *, and numbers.

        >>> nested_expr = Pair('+', Pair(Pair('*', Pair(3, Pair(4, nil))), Pair(5, nil)))
        >>> print_evals(nested_expr)
        (+ (* 3 4) 5)
        +
        (* 3 4)
        *
        3
        4
        5
        >>> print_evals(Pair('*', Pair(6, Pair(7, Pair(nested_expr, Pair(8, nil))))))
        (* 6 7 (+ (* 3 4) 5) 8)
        *
        6
        7
        (+ (* 3 4) 5)
        +
        (* 3 4)
        *
        3
        4
        5
        8
        """
        if not isinstance(expr, Pair):
                print(expr)
        else:
            print(expr)
            print(expr.first)
            cur = expr.rest
            while cur:
                print_evals(cur.first)
                cur = cur.rest

def after(s, a, b):
    """Return whether b comes after a in linked list s.
    >>> t = Link(3, Link(6, Link(5, Link(4))))
    >>> after(t, 6, 4)
    True
    >>> after(t, 4, 6)
    False
    >>> after(t, 6, 6)
    False
    """
    def find(s, n, f):
        if s == Link.empty:
            return False
        elif s.first == n:
            return f(s.rest)
        else:
            return find(s.rest, n, f)
    return find(s, a, lambda rest: find(rest, b, lambda rest: True))

class Link:
    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link), "rest must be a Link or Link.empty"
        self.first = first
        self.rest = rest

    def __str__(self):
        string = '<'
        current = self      
        while current is not Link.empty:
            string += str(current.first)
            current = current.rest
            if current is not Link.empty:
                string += ', '
        string += '>'
        return string  
    
    def __repr__(self):
        if self.rest is Link.empty:
            return f'Link({self.first})'
        else:
            return f'Link({self.first}, {self.rest})'

    def __len__(self):
        if self.rest is Link.empty:
            return 1
        else:
            return 1 + len(self.rest)

