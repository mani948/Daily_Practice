t = int(input())

for _ in range(t):
    n, c, m = map(int, input().split())
    
    chocolates = n // c
    wrappers = chocolates
    
    while wrappers >= m:
        free = wrappers // m
        chocolates += free
        wrappers = wrappers % m + free
    
    print(chocolates)