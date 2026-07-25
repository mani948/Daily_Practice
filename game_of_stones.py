def gameOfStones(n):
    if n % 7 == 0 or n % 7 == 1:
        return "Second"
    return "First"


t = int(input())

for _ in range(t):
    n = int(input())
    print(gameOfStones(n))