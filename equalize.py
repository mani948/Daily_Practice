n = int(input().strip())
arr = list(map(int, input().strip().split()))

freq = {}


for x in arr:
    freq[x] = freq.get(x, 0) + 1


max_freq = max(freq.values())

print(n - max_freq)