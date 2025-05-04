#List
from operator import getitem,add,mul
digits=[1,8,2,8]
len(digits)
digits[3] == getitem(digits,3)
add([2,7],mul(digits,2))
digit=[[1,2],[3,4]]
digit[1][0]==3
"""
>>> 1 in digits
True
>>> 5 not in digits
True
"""
#For Statment
def count(s,value):
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total
def pair(pair):
    same_count=0
    for x,y in pair:
        if x==y:
            same_count+=1
    return same_count
"""
>>> list(range(-2,2))
[-2,-1,0,1]
>>> list(range(4))
[0,1,2,3]
"""
"""
odds=[1,3,5,7,9]
>>> [x+1 for x in odds]
[2,4,6,8,10]
"""
def divisors(n):
    return [x for x in range(1,n) if n%x==0]