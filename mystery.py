def theLoveLetterMystery(s):
    count = 0
    i = 0
    j = len(s) - 1

    while i < j:
        count += abs(ord(s[i]) - ord(s[j]))
        i += 1
        j -= 1

    return count


q = int(input())

for _ in range(q):
    s = input().strip()
    print(theLoveLetterMystery(s))