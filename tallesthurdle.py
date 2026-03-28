n, k = map(int, input().split())
h = list(map(int, input().split()))

print(max(0, max(h) - k))