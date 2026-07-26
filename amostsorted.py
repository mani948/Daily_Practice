def almostSorted(arr):
    sorted_arr = sorted(arr)

    
    diff = []
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            diff.append(i)

   
    if not diff:
        print("yes")
        return

    l = diff[0]
    r = diff[-1]

  
    temp = arr[:]
    temp[l], temp[r] = temp[r], temp[l]

    if temp == sorted_arr:
        print("yes")
        print(f"swap {l + 1} {r + 1}")
        return

    temp = arr[:]
    temp[l:r + 1] = reversed(temp[l:r + 1])

    if temp == sorted_arr:
        print("yes")
        print(f"reverse {l + 1} {r + 1}")
        return

    print("no")



n = int(input())
arr = list(map(int, input().split()))

almostSorted(arr)