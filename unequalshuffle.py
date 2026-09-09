T = int(input())

for _ in range(T):
    N = int(input())
    A = input()
    B = input()

    if A.count('a') + B.count('a') == N:
        print("YES")
    else:
        print("NO")