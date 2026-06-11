def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def palindromeIndex(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:

            if is_palindrome(s, i + 1, j):
                return i

            if is_palindrome(s, i, j - 1):
                return j

            return -1

        i += 1
        j -= 1

    return -1


q = int(input())

for _ in range(q):
    s = input().strip()
    print(palindromeIndex(s))