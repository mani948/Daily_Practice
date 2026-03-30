h = list(map(int, input().split()))
word = input()

max_height = max(h[ord(c) - ord('a')] for c in word)
print(max_height * len(word))