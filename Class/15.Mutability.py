#Object
from datetime import date
today=date(2025,2,24)
freedom =date(2025,6,24)
today
str(freedom-today)
"""
'120 days, 0:00:00' """
today.year==2025
today.month==2
today.strftime('%A %B %d')
"""
>>> today.strftime('%A %B %d')
'Monday February 24"""
s='Hello'
s.upper()
s.lower()
s.swapcase()
a='A'
ord(a)==65
hex(ord(a))==41
print('\a\a\a')
print('\n\n\n')
from unicodedata import lookup,name
name('A')
lookup('WHITE SMILING FACE')

numerals ={'I':1,'V':5,'X':10}
numerals['x']=11
numerals['L']=50
numerals.pop('x')

four=[1,2,3,4]
four.append(5)
four.extend([6])
print(four)
#Tuples:immutable values
tuple=(1,2,3,4,5)
tuple=(2,)
a=[10]
b=[10]
"""
>>> a is b
False"""

#Mutable default values are dangerous!
def f(s=[]):
    s.append(5)
    return len(s)
"""
>>> f()
1
>>> f()
2
>>> f()
3 """

#Mutable Functions&Persistent local state
def make_withdraw_list(balance):
    b=[balance]
    def withdraw(amount):
        if amount> b[0]:
            return 'Insufficient funds'
        b[0]=b[0]-amount
        return b[0]
    return withdraw

withdraw = make_withdraw_list(100)
withdraw(25)

