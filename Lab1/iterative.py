import sys
def fib2(n):
    if n == 0: return 0
    arr = [0] * (n+1)
    arr[0] = 0
    arr[1] = 1
    i = 2
    while(i <= n):
        arr[i] = arr[i-1]+arr[i-2]
        i+=1
    return arr[n]


n = int(sys.argv[1])
x = 0
while(x < 999999):
    fib2(n)
    x+=1
print(fib2(n))
