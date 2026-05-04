n,t=map(int,input().split())

w=list(map(int,input().split()))
for _ in range(t):
    i,j=map(int,input().split())
    
    print(min(w[i:j+1]))
    