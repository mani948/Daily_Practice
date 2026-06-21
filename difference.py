def minimumAbsoluteDifference(arr):
    arr.sort()
    ans = float('inf')

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        ans = min(ans, diff)

    return ans

n=int(input())
arr=list(map(int,input().split()))

print(minimumAbsoluteDifference(arr))