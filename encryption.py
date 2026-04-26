s = input().strip().replace(" ", "")
n = len(s)

r = int(n ** 0.5)
c = r

if r * c < n:
    c += 1
if r * c < n:
    r += 1

ans = []

for i in range(c):
    word = ""
    for j in range(i, n, c):
        word += s[j]
    ans.append(word)

print(" ".join(ans))