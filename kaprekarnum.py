p = int(input())
q = int(input())

found = False

for n in range(p, q + 1):
    sq = str(n * n)
    d = len(str(n))
    
    right = sq[-d:]         
    left = sq[:-d]          
    
    if left == "":
        left_num = 0
    else:
        left_num = int(left)
    
    right_num = int(right)
    
    if left_num + right_num == n:
        print(n, end=" ")
        found = True

if not found:
    print("INVALID RANGE")