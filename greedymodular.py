n, k = map(int, input().split())
S = list(map(int, input().split()))

count = [0] * k

for num in S:
    count[num % k] += 1


result = 0


if count[0] > 0:
    result += 1


for i in range(1, (k // 2) + 1):
    if i != k - i:
        result += max(count[i], count[k - i])
    else:
        if count[i] > 0:
            result += 1

print(result)