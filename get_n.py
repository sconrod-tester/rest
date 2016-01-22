
n = input("Enter a positive numerical value: ")
if n >= 0:
    print n
elif n < 0 and n != 0:
    print "Error you have entered a negative value please enter a positive value"
else:
    exit             

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b, a+b
 return a
print fib(n)
