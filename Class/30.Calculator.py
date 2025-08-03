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



