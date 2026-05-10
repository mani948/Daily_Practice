t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    inv = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                inv += 1
    
    print("YES" if inv % 2 == 0 else "NO")