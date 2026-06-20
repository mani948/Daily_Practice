def largestPermutation(k, arr):
    n = len(arr)

    
    pos = {}
    for i in range(n):
        pos[arr[i]] = i

    for i in range(n):
        if k == 0:
            break

        expected = n - i   

       
        if arr[i] == expected:
            continue

       
        idx = pos[expected]

        
        pos[arr[i]] = idx
        pos[expected] = i

       
        arr[i], arr[idx] = arr[idx], arr[i]

        k -= 1

    return arr


n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = largestPermutation(k, arr)
print(*ans)