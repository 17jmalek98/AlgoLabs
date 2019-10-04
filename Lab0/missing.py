#for a list of incrementing numbers 1 to x, find the missing number in the sequence.
#uses the sum formula, (x * (x+1))/2 = sum of first x numbers
arr = [6,5,4,1,2]
maxi = 0
total = 0
for x in arr:
    if(x >= maxi):
        maxi = x
    total += x

expect = maxi*(maxi+1)/2
print(expect-total)
