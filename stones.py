t = int(input())

for i in range(t):
    n = int(input())
    a = int(input())
    b = int(input())

    s = set()

    for j in range(n):
        x = (n - 1 - j) * a + j * b
        s.add(x)

    print(*sorted(s))