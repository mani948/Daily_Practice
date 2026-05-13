n=int(input())
arr=[]
for _ in range(n):
    arr.append(input().strip())


arr.sort(key=lambda x: (len(x),x))

for num in arr:
    print(num)