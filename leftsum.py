def balancedSums(arr):
    total = sum(arr)
    left = 0

    for x in arr:
        if left == total - left - x:
            return "YES"
        left += x

    return "NO"


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(balancedSums(arr))