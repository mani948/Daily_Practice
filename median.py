def findMedian(arr):
    arr.sort()
    return arr[len(arr) // 2]

n = int(input())
arr = list(map(int, input().split()))

print(findMedian(arr))