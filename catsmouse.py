n = int(input())

for i in range(n):
    x, y, z = map(int, input().split())

    d1 = abs(x - z)
    d2 = abs(y - z)

    if d1 < d2:
        print("Cat A")
    elif d2 < d1:
        print("Cat B")
    else:
        print("Mouse C")