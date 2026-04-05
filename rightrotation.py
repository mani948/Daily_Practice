n, k, q = map(int, input().split())

a = list(map(int, input().split()))

k = k % n


rotated = [0] * n


for i in range(n):
    new_index = (i + k) % n
    rotated[new_index] = a[i]

for _ in range(q):
    index = int(input())
    print(rotated[index])