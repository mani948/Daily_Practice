n, k = map(int, input().split())
arr = list(map(int, input().split()))

page = 1
count = 0

for problems in arr:
    i = 1
    while i <= problems:
        end = min(i + k - 1, problems)
        
        if page >= i and page <= end:
            count += 1
        
        page += 1
        i += k

print(count)