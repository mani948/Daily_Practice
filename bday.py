t = int(input())

for i in range(t):
    b, w = map(int, input().split())
    bc, wc, z = map(int, input().split())


    black_cost = min(bc, wc + z)

 
    white_cost = min(wc, bc + z)

    total = b * black_cost + w * white_cost

    print(total)