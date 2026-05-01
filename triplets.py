n,d=map(int,input().split())
arr=list(map(int,input().split()))

s=set(arr)
count=0
for x in arr:
    if (x + d in s) and (x + 2*d in s):
        count+=1
        
print(count)