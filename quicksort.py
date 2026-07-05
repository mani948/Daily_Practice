def quickSort(arr):
    pivot = arr[0]   
    left = []
    equal = [pivot]
    right = []
    
    for x in arr[1:]:   
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
    
    return left + equal + right


n = int(input().strip())
arr = list(map(int, input().split()))
result = quickSort(arr)
print(*result)
