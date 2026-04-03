n = int(input())

shared = 5
total_likes = 0

for i in range(1, n + 1):
    liked = shared // 2
    total_likes = total_likes + liked
    shared = liked * 3

print(total_likes)