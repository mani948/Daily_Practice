n = int(input())
arr = list(map(int, input().split()))

last_seen = {}
min_dist = float('inf')

for i in range(n):
    if arr[i] in last_seen:
        min_dist = min(min_dist, i - last_seen[arr[i]])
    last_seen[arr[i]] = i

print(min_dist if min_dist != float('inf') else -1)