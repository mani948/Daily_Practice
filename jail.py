t = int(input())

for i in range(t):
    n, m, s = map(int, input().split())

    result = (s + m - 1) % n

    if result == 0:
        result = n

    print(result)