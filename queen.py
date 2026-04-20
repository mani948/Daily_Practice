n, k = map(int, input().split())
rq, cq = map(int, input().split())

# max moves in 8 directions
up = n - rq
down = rq - 1
right = n - cq
left = cq - 1
ur = min(up, right)
ul = min(up, left)
dr = min(down, right)
dl = min(down, left)

for _ in range(k):
    r, c = map(int, input().split())

    if c == cq:   # same column
        if r > rq:
            up = min(up, r - rq - 1)
        else:
            down = min(down, rq - r - 1)

    elif r == rq:   # same row
        if c > cq:
            right = min(right, c - cq - 1)
        else:
            left = min(left, cq - c - 1)

    elif abs(r - rq) == abs(c - cq):   # diagonal
        if r > rq and c > cq:
            ur = min(ur, r - rq - 1)
        elif r > rq and c < cq:
            ul = min(ul, r - rq - 1)
        elif r < rq and c > cq:
            dr = min(dr, rq - r - 1)
        else:
            dl = min(dl, rq - r - 1)

print(up + down + left + right + ur + ul + dr + dl)