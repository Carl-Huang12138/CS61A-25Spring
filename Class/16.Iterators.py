s = [3,4,5]
u = iter(s)
"""
>>>next(u)
3
>>>list(u)
[4,5]
>>>next(u)
Error"""
d={'one':1,'two':2,'three':3}
d['zero']=0
k= iter(d.keys()) #or iter(d)
v =iter(d.values())
i=iter(d.items())

def double(x):
    print('**',x,'=>',2*x,'**')
    return 2*x

m=map(double,[3,4,5])
f=lambda y:y>=10
t=filter(f,m)
next(t)

def palindrome(s):
    """Return whether s is the same backward and forward """
    return all([a==b for a,b in zip(s,reversed(s))])

