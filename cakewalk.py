def marcsCakewalk(arr):
    arr.sort(reverse=True)
    return sum(c * (1 << i) for i, c in enumerate(arr))
    
n=int(input())
arr=list(map(int,input().split()))
print(marcsCakewalk(arr))