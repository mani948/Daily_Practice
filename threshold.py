t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    ontime=0
    
    for j in arr:
        if j<=0:
            ontime+=1
            
    if ontime<k:
        print("YES")
    else:
        print("NO")
            