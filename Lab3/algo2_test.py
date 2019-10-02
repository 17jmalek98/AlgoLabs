import random
def partition(a, p, r, pivot):
    """
    Permutes the elements of a[p..r] (inclusive) in-place:
       first elements <= a[r], then a[r], then those > a[r].
    Returns the new location (index) of pivot value a[r] in the array.
    """
    i = p - 1
    for j in range(p, r + 1):
        if a[j] < pivot:
            i = i + 1
            a[i], a[j] = a[j], a[i]

    return i

def mom(a, left, right):
    """
    Returns the median of medians for array a.
    """
    length = right - left + 1
    if length <= 0:
        return
    if length <= 5:
        return sorted(a[left : right + 1])[length/2]

    num_of_medians = length/5
    medians = [mom(a, left + 5*i, left + 5 * (i + 1) - 1) for i in range(num_of_medians)]
    return mom(medians, 0, len(medians) - 1)

def kth(a, left, right, k):
    """
    ~~~~~
    NOTE: k here means k-th smallest element. So in an array of length 10, the
    k-th smallest element is the (len(array) - k)-th largest element.
    ~~~~~

    Partitions the array a around the median of medians pivot. Keeps finding new
    pivots until the pivot == k. Then the partition is around k.
    then a[(len(a) - k)...(len(a)-1)] will output the largest k elements (not sorted)
    """
    pivotIndex = mom(a, left, right)

    pivotIndex = partition(a, left, right, pivotIndex)

    while k != pivotIndex + 1:

        if k > pivotIndex + 1:
            pivotIndex = kth(a, pivotIndex + 1, right, k)

        elif k < pivotIndex + 1:
            pivotIndex = kth(a, left, pivotIndex, k)

    return pivotIndex #this is index of the kth largest elemen

arr = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15];
k = 10;
newarr = [];
for i in range(10000000):
    newarr.append(random.randint(0,100000))

#median_of_medians(newarr,5000000);
print Select(arr,k);
