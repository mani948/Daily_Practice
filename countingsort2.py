def countingSort(arr):
  
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])
    return result



n = int(input().strip())
arr = list(map(int, input().split()))

sorted_arr = countingSort(arr)
print(" ".join(map(str, sorted_arr)))
