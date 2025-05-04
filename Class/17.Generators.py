def even(start,end):
    even = even +(even%2)
    while even<end:
        yield even
        even+=2

def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])

def partitions(n,m):
    if n>0 and m>0:
        if n == m:
            yield str(m)
        for p in partitions(n-m,m):
            yield p +'+'+ str(m)
        yield from partitions(n,m-1)

for p in partitions(6,4):
     print(p)