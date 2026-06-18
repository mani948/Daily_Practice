def luckBalance(k, contests):
    imp = []
    ans = 0

    for l, t in contests:
        if t == 0:
            ans += l
        else:
            imp.append(l)

    imp.sort(reverse=True)

    ans += sum(imp[:k])
    ans -= sum(imp[k:])

    return ans


n, k = map(int, input().split())
contests = []

for _ in range(n):
    l, t = map(int, input().split())
    contests.append([l, t])

print(luckBalance(k, contests))