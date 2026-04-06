s = input().strip()  
t = input().strip()  
k = int(input().strip())  


common_length = 0
for i in range(min(len(s), len(t))):
    if s[i] == t[i]:
        common_length += 1
    else:
        break


min_ops = (len(s) - common_length) + (len(t) - common_length)


if k < min_ops:
    print("No")
elif (k - min_ops) % 2 == 0:
    print("Yes")
elif k >= len(s) + len(t):
    print("Yes")
else:
    print("No")