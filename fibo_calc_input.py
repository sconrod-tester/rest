

from get_n import n
print get_n()
n = get_n()




def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print fib(9)
