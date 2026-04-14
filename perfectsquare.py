import math

def squares(a, b):
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    
    count = end - start + 1
    
    if count < 0:
        return 0
    return count



t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(squares(a, b))