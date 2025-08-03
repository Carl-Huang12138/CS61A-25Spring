def min_abs_indices(s):
    """Return a list of indices of the minimum absolute value in s."""
    min_value = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_value]

def largest_adjacent_sum(s):
    """Return the largest sum of two adjacent elements in s."""
    return max([s[i-1] + s[i] for i in range(1, len(s))])
"""
    #Method 2
    return max([a + b for a, b in zip(s[:-1], s[1:])])
    """

def digit_dict(s):
    """Return a dictionary mapping the last digit of each number in s to a list of numbers with that last digit."""
    dict = {}
    for r in s:
        digit = r % 10
        if digit not in dict:
            dict[digit] = [r]
        else:
            dict[digit].append(r)
    return dict
"""
    #Method 2
    return {d: [x for x in s if x % 10 == d] for d in range(10) if any([x%10 == d for x in s]) }
    """
def all_have_equal(s):
    dict = {}
    for r in s:
        if r not in dict:
            dict[r] = False
        else:
            dict[r] = True
    return all(dict.values())
"""    #Method 2
    return min([s.count(x) for x in s]) > 1"""

#Linked Lists Exercises
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
    
def ordered(s, key = lambda x: x):
    if s is Link.empty or s.rest is Link.empty:
        return True
    elif key(s.first) <= key(s.rest.first):
        return ordered(s.rest, key)
    else:
        return False
    
def merge(s1, s2, key = lambda x: x):
    """Merge two ordered links into one ordered link."""
    if s1 is Link.empty:
        return s2
    elif s2 is Link.empty:
        return s1
    elif key(s1.first) <= key(s2.first):
        return Link(s1.first, merge(s1.rest, s2, key))
    else:
        return Link(s2.first, merge(s1, s2.rest, key))
    
def merge_in_place(s1, s2, key = lambda x: x):
    """Merge two ordered links into one ordered link in place."""
    if s1 is Link.empty:
        return s2
    elif s2 is Link.empty:
        return s1
    elif key(s1.first) <= key(s2.first):
        s1.rest = merge_in_place(s1.rest, s2, key)
        return s1
    else:
        s2.rest = merge_in_place(s1, s2.rest, key)
        return s2

