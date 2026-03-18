n=int(input())
arr=list(map(int,input().split()))
count=[0,0,0,0,0,0]

for i in arr:
    count[i]+=1
    
maxx=max(count)
result=0
for i in range(1,6):
    if count[i]==maxx:
        result=i
        break       
print(result)