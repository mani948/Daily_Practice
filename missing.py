from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
brr = list(map(int, input().split()))

c1 = Counter(arr)
c2 = Counter(brr)

ans = []

for x in sorted(c2):
    if c1[x] != c2[x]:
        ans.append(x)

print(*ans)