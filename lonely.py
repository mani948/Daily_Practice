def lonelyinteger(a):
    r = 0
    for x in a:
        r ^= x
    return r

n = int(input())
a = list(map(int, input().split()))
print(lonelyinteger(a))