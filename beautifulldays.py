i, j, k = map(int, input().split())

count = 0

for day in range(i, j + 1):
    reverse_day = int(str(day)[::-1])   
    diff = abs(day - reverse_day)       

    if diff % k == 0:                   
        count += 1

print(count)