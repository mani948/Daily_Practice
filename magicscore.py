s = []

for _ in range(3):
    row = list(map(int, input().split()))
    s.append(row)

magic = [
    [[8,3,4],[1,5,9],[6,7,2]],
    [[6,1,8],[7,5,3],[2,9,4]],
    [[4,9,2],[3,5,7],[8,1,6]],
    [[2,7,6],[9,5,1],[4,3,8]],
    [[8,1,6],[3,5,7],[4,9,2]],
    [[4,3,8],[9,5,1],[2,7,6]],
    [[6,7,2],[1,5,9],[8,3,4]],
    [[2,9,4],[7,5,3],[6,1,8]]
]

min_cost = float('inf')

for m in magic:
    cost = 0
    
    for i in range(3):
        for j in range(3):
            cost += abs(s[i][j] - m[i][j])
    
    if cost < min_cost:
        min_cost = cost

print(min_cost)