n = int(input())
p = list(map(int, input().split()))

for x in range(1, n + 1):


    for i in range(n):
        if p[i] == x:
            pos1 = i + 1

  
    for j in range(n):
        if p[j] == pos1:
            pos2 = j + 1

    print(pos2)