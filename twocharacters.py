n = int(input())
s = input()

ans = 0
chars = set(s)

for a in chars:
    for b in chars:

        if a != b:

            t = ""

            for ch in s:
                if ch == a or ch == b:
                    t += ch

            ok = True

          
            for i in range(len(t) - 1):

                if t[i] == t[i + 1]:
                    ok = False
                    break

           
            if ok and len(t) > 1:

                if len(t) > ans:
                    ans = len(t)

print(ans)