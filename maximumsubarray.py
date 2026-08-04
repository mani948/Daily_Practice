from bisect import bisect_right, insort

def maximumSum(a, m):
    pref = ans = 0
    s = []
    for x in a:
        pref = (pref + x) % m
        ans = max(ans, pref)
        i = bisect_right(s, pref)
        if i < len(s):
            ans = max(ans, (pref - s[i] + m) % m)
        insort(s, pref)
    return ans

q = int(input())
for _ in range(q):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(maximumSum(a, m))