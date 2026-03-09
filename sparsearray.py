n = int(input())
stringList = []

for i in range(n):
    s = input()
    stringList.append(s)

q = int(input())

for i in range(q):
    query = input()
    count = 0

    for s in stringList:
        if s == query:
            count += 1

    print(count)