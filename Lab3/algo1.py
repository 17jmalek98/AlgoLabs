import random
def recurse(arr,k):
    v = random.choice(arr);
    print(v);
    sl = [];
    sr = [];
    sv = [];
    for x in range(0, len(arr)):
        if(arr[x] == v):
            sv.append(arr[x]);
        elif(arr[x] < v):
            sl.append(arr[x]);
        else:
            sr.append(arr[x]);
    #print(sl);
    #print(sv);
    #print(sr);

    if(k <= len(sl)):
        print("in sl array");
        recurse(sl,k);
    elif(len(sl) < k and k <= len(sl) + len(sv)):
        print("kth smallest is "+ str(v));
    else:
        print("in sr array");
        recurse(sr, k-len(sl)-len(sv));




arr = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15];
k = 10;

newarr = [];
for i in range(10000000):
    newarr.append(random.randint(0,100000))

#recurse(newarr,5000000);
recurse(arr,k);
#time is 32s to complete
