from cache import cache

def fibo(n):
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a+b
    return a

@cache
def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-1) + fibo(n-2)

if __name__ == '__main__':

    for i in range(200):
        print i, '-->', fibo(i)
