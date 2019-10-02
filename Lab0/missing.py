arr = [6,5,4,1,2]
maxi = 0
total = 0
for x in arr:
    if(x >= maxi):
        maxi = x
    total += x

expect = maxi*(maxi+1)/2
print(expect-total)
