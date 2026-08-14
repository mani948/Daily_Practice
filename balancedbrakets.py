def isBalanced(s):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:
        if ch in "([{":
            stack.append(ch)

        else:
            if len(stack) == 0:
                return "NO"

            if stack[-1] != pairs[ch]:
                return "NO"

            stack.pop()

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


n = int(input())

for _ in range(n):
    s = input()
    print(isBalanced(s))