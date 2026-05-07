t = int(input())

for _ in range(t):

    n = int(input())
    s = input()

    if "_" in s:

        d = {}

        for i in s:
            if i != "_":
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1

        ok = True

        for i in d:
            if d[i] == 1:
                ok = False
                break

        if ok:
            print("YES")
        else:
            print("NO")

    else:

        ok = True

        for i in range(n):

            left = False
            right = False

            if i > 0 and s[i] == s[i-1]:
                left = True

            if i < n-1 and s[i] == s[i+1]:
                right = True

            if not left and not right:
                ok = False
                break

        if ok:
            print("YES")
        else:
            print("NO")