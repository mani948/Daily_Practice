t = int(input())   

for _ in range(t):
    n = int(input())   
    height = 1

    for cycle in range(1, n + 1):
        if cycle % 2 == 1:     
            height = height * 2
        else:                  
            height = height + 1

    print(height)