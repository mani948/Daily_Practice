n=int(input())
b=list(map(int,input().split()))

c=0

for i in range(n-1):
    if b[i]%2!=0:
        b[i]+=1
        b[i+1]+=1
        c+=2

if sum(b)%2!=0:
    print("NO")
else:
    print(c)