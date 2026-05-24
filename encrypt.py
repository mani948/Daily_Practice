n = int(input())
s = input()
k = int(input())

k %= 26
ans = ""

for ch in s:
    if 'a' <= ch <= 'z':
        ans += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))

    elif 'A' <= ch <= 'Z':
        ans += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))

    else:
        ans += ch

print(ans)