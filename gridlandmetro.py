from collections import defaultdict

def gridlandMetro(n, m, k, track):
    d = defaultdict(list)

    for r, c1, c2 in track:
        d[r].append((c1, c2))

    occupied = 0

    for intervals in d.values():
        intervals.sort()
        s, e = intervals[0]

        for c1, c2 in intervals[1:]:
            if c1 <= e:
                e = max(e, c2)
            else:
                occupied += e - s + 1
                s, e = c1, c2

        occupied += e - s + 1

    return n * m - occupied

n, m, k = map(int, input().split())

track = [list(map(int, input().split())) for _ in range(k)]

print(gridlandMetro(n, m, k, track))
