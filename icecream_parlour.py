def icecreamParlor(m, cost):
    seen = {}

    for i in range(len(cost)):
        complement = m - cost[i]

        if complement in seen:
            return [seen[complement] + 1, i + 1]  
        seen[cost[i]] = i



t = int(input())

for _ in range(t):
    m = int(input())
    n = int(input())
    cost = list(map(int, input().split()))

    result = icecreamParlor(m, cost)
    print(result[0], result[1])