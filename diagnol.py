n=int(input())

arr=[]

for i in range(n):
    row=list(map(int,input().split()))
    arr.append(row)
    
    
primar=0
second=0

for i in range(n):
    primar+=arr[i][i]
    second+=arr[i][n-i-1]
    
    
result=abs(primar-second)

print(result)
    
    
    


    
    
    
    
