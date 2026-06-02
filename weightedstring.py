def weightedUniformStrings(s, queries):
    weights = set()

    current = 0
    prev = ''

    for ch in s:
        val = ord(ch) - ord('a') + 1

        if ch == prev:
            current += val
        else:
            current = val

        weights.add(current)
        prev = ch

    return ["Yes" if q in weights else "No" for q in queries]


s = input().strip()
n = int(input())

queries = []
for _ in range(n):
    queries.append(int(input()))

result = weightedUniformStrings(s, queries)

for ans in result:
    print(ans)