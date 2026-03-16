n=int(input())
scores=list(map(int,input().split()))
max_score=scores[0]
min_score=scores[0]
maxx=0
minn=0

for i in range(1,n):
    
    if scores[i]>max_score:
        max_score=scores[i]
        maxx+=1
        
    elif scores[i]<min_score:
        min_score=scores[i]
        minn+=1
        
print(maxx,minn)