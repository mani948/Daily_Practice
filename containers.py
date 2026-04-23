q = int(input())

for _ in range(q):
    n = int(input())
    a = []

    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)

    x = []   
    y = [0] * n   

    for i in range(n):
        x.append(sum(a[i]))

    for i in range(n):
        for j in range(n):
            y[j] += a[i][j]

    if sorted(x) == sorted(y):
        print("Possible")
    else:
        print("Impossible")