def maximumPerimeterTriangle(sticks):
    sticks.sort()

    for i in range(len(sticks) - 1, 1, -1):
        a, b, c = sticks[i - 2], sticks[i - 1], sticks[i]

        if a + b > c:
            return [a, b, c]

    return [-1]



n = int(input())
sticks = list(map(int, input().split()))

ans = maximumPerimeterTriangle(sticks)

if ans == [-1]:
    print(-1)
else:
    print(*ans)