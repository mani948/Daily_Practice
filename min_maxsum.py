arr=list(map(int,input().split()))

total=sum(arr)

print(total-max(arr),total-min(arr))
