#Measuring Efficiency
def count(f):
    def counted(n):
        counted.calls += 1
        return f(n)
    counted.calls = 0
    return counted

@count
def fib(n):
    if n == 0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
#Memorization
def memo(f):
    cache = {}
    def memorized(n):
        if n not in cache:
            cache[n] = f(n)
            return cache[n]
    return memorized                #Same behaviur as f, if f is a pure function

#Exponention
def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)
    
def exp_fast(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = exp_fast(b, n // 2)
        return half * half
    else:
        return b * exp_fast(b, n - 1)  # n is odd, so we reduce it by 1 and multiply by b

#Space
def count_frames(f):
    def counted(n):
        counted.frames += 1
        if counted.frames > counted.max_frames:
            counted.max_frames = counted.frames
        result = f(n)
        counted.frames -= 1
        return result
    counted.frames = 0
    counted.max_frames = 0
    return counted