n=int(input())
arr=list(map(int,input().split()))
pos=0
neg=0
zer=0


for i in arr:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zer+=1
       
        
print(f"{pos/n:.6f}")
print(f"{neg/n:.6f}")
print(f"{zer/n:.6f}") 
        