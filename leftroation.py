a,d=map(int,input().split())
arr=list(map(int,input().split()))

d=d%a

result=arr[d:]+arr[:d]

print(*result)