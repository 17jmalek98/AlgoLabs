import sys
def fib1(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib1(n-1) + fib1(n-2)


n = int(sys.argv[1])
print(fib1(n))
