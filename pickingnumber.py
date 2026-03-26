n = int(input())
a = list(map(int, input().split()))

freq = [0] * 101


for num in a:
    freq[num] += 1

max_len = 0


for i in range(100):
    length = freq[i] + freq[i+1]
    
    if length > max_len:
        max_len = length

print(max_len)