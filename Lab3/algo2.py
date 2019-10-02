import random
def select(arr, k):
    v = part(arr,k);
    print(v)
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

    if(k <= len(sl)):
        print("in sl array");
        return select(sl,k);
    elif(k > len(sl) +len(sv)):
        print("in sr array");
        return select(sr, k-len(sl)-len(sv));
    else:
        print("kth smallest is "+ str(v));
        return v;

def part(arr, k):
    #print("Called")
    if(len(arr) <= 10):
        #print("little array")
        arr.sort();
        #print(arr[len(arr)/2]);
        return arr[len(arr)/2];

    empty_lists = [[] for i in xrange(len(arr)/5)];
    medians = [];
    x = -1;
    for i in xrange((len(arr))):
        if((i) % 5 == 0 and x < len(arr)/5-1):
            x+=1;
        #print(arr[i]);
        empty_lists[x].append(arr[i]);
    #print(empty_lists)
    for i in xrange(len(arr)/5):
        medians.append(part(empty_lists[i],3));
    #print(medians)
    v = part(medians, len(arr)/10)
    return v;


arr = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15];
narr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];
k = 15;
newarr = [];
for i in range(10000000):
    newarr.append(random.randint(0,100000))


#print select(newarr,5000000);
print select(arr,10);
#time 45s
