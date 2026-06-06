from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

    c1 = Counter(s1)
    c2 = Counter(s2)

    return sum((c1 - c2).values())

t = int(input())

for _ in range(t):
    s = input().strip()
    print(anagram(s))