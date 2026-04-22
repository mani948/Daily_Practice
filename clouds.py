n = int(input())
c = list(map(int, input().split()))

i = 0
j = 0

while i < n - 1:
    if i + 2 < n and c[i + 2] == 0:
        i += 2
    else:
        i += 1
    j += 1

print(j)