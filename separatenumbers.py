def separateNumbers(s):
    n = len(s)

    
    for i in range(1, n // 2 + 1):

        first = int(s[:i])
        temp = ""
        current = first

        
        while len(temp) < n:
            temp += str(current)
            current += 1

       
        if temp == s:
            print("YES", first)
            return

    print("NO")



q = int(input())

for _ in range(q):
    s = input().strip()
    separateNumbers(s)