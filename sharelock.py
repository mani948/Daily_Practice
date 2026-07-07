
def decentNumber(n):

    fives = n
    while fives % 3 != 0:
        fives -= 5
    if fives < 0:
        print(-1)
    else:
        threes = n - fives
        print("5" * fives + "3" * threes)

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    decentNumber(n)
