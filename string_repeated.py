s = input().strip()
n = int(input())

count_a = s.count('a')

full = n // len(s)
rem = n % len(s)

result = count_a * full + s[:rem].count('a')

print(result)