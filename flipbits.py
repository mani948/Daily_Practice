def flippingBits(n):
    return 4294967295 - n

q = int(input())

for _ in range(q):
    n = int(input())
    print(flippingBits(n))