def toys(w):
    w.sort()

    containers = 0
    i = 0
    n = len(w)

    while i < n:
        containers += 1
        limit = w[i] + 4

        while i < n and w[i] <= limit:
            i += 1

    return containers
n=int(input())
w=list(map(int,input().split()))
print(toys(w))