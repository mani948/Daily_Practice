q = int(input())

for _ in range(q):
    s = input()
    r = s[::-1]

    if all(abs(ord(s[i]) - ord(s[i+1])) == abs(ord(r[i]) - ord(r[i+1]))
           for i in range(len(s)-1)):
        print("Funny")
    else:
        print("Not Funny")