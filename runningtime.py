n = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(1, n):
    temp = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > temp:
        arr[j + 1] = arr[j]
        count += 1
        j -= 1

    arr[j + 1] = temp

print(count)