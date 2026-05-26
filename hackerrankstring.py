def hackerrankInString(s):
    word = "hackerrank"
    j = 0

    for ch in s:
        if j < len(word) and ch == word[j]:
            j += 1

    if j == len(word):
        return "YES"
    else:
        return "NO"


q = int(input())

for _ in range(q):
    s = input()
    print(hackerrankInString(s))