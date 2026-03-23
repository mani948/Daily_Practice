b, n, m = map(int, input().split())

keyboards = list(map(int, input().split()))
drives = list(map(int, input().split()))

max_cost = -1

for i in range(n):
    for j in range(m):
        total = keyboards[i] + drives[j]

        if total <= b and total > max_cost:
            max_cost = total

print(max_cost)