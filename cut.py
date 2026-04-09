n = int(input())
arr = list(map(int, input().split()))

arr.sort()

while len(arr) > 0:
    print(len(arr))
    
    m = arr[0]
    
    for i in range(len(arr)):
        arr[i] = arr[i] - m
    
    arr = [x for x in arr if x > 0]