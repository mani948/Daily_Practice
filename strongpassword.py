n = int(input())
password = input()

digit = False
lower = False
upper = False
special = False

special_chars = "!@#$%^&*()-+"

for ch in password:
    if ch.isdigit():
        digit = True
    elif ch.islower():
        lower = True
    elif ch.isupper():
        upper = True
    elif ch in special_chars:
        special = True

missing = 0

if not digit:
    missing += 1
if not lower:
    missing += 1
if not upper:
    missing += 1
if not special:
    missing += 1


answer = max(missing, 6 - n)

print(answer)