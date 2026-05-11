t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if k == 0:
        for i in range(1, n + 1):
            print(i, end=" ")
        print()

    elif n % (2 * k) != 0:
        print(-1)

    else:
        add = True

        for i in range(1, n + 1):

            if add:
                print(i + k, end=" ")
            else:
                print(i - k, end=" ")

            if i % k == 0:
                add = not add

        print()