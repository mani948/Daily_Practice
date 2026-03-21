n=int(input())
arr=list(map(int,input().split()))
count={}
pairs=0

for sock in arr:
    if sock in count:
        count[sock]+=1
    else:
        count[sock]=1
        
        
for c in count:
    pairs=pairs+count[c]//2
    
print(pairs)
    