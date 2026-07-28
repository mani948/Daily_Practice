def candies(n, arr):
    c = [1] * n

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            c[i] = c[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            c[i] = max(c[i], c[i + 1] + 1)

    return sum(c)


n = int(input())
arr = [int(input()) for _ in range(n)]

print(candies(n, arr))