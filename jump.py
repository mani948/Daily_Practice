n, k = map(int, input().split())
c = list(map(int, input().split()))

e = 100
i = 0

while True:
    i = (i + k) % n
    e -= 1
    
    if c[i] == 1:
        e -= 2
    
    if i == 0:
        break

print(e)