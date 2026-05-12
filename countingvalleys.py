steps = int(input())
path = input()

level = 0
valleys = 0

for i in path:
    if i == 'U':
        level += 1
        if level == 0:
            valleys += 1
    else:
        level -= 1

print(valleys)