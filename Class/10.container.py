odds=[1,3,5,7,9]
[odds[i] for i in range(1,3)]
odds[1:3]
'''
>>> sum([2,3,4],5)
14
>>> sum([[2,3],[4]],[])
[2,3,4]
>>> max(range(10),key= lambda x: 7-(x-2)*(x-4))
3
>>> all([x<5 for x in range(5)])
True
'''
#Dictionary
numerals ={'I':1,'V':5,'X':10}
"""
>>> numerals['V']
5
>>> numerals.value()
dict_values([1,5,10])"""
{x*x:x for x in [1,2,3,4,5] if x>2}

def index(keys,values,match):
    """Return a dictionary from keys k to a list of values v 
    for which match(k,v) is  a true value.
    >>> index([7,9,11],range(30,50),lambda k,v : v%k == 0)
    {7:[35,42,49],9:[36,45],11:[33,44]}
    """
    return {k:[v for v in values if match(k,v)] for k in keys}