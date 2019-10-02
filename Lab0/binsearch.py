def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:
                return -1
            lower = x
        elif target < val:
            upper = x

arr = [1,2,3,4,6,8,9,10]
print("num exists at index: " + str(binary_search(arr,11)))
