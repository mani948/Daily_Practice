s = input()

hour = int(s[:2])
minute = s[3:5]
second = s[6:8]
period = s[8:]

if period == "AM":
    if hour == 12:
        hour = 0
else:   
    if hour != 12:
        hour = hour + 12

print(f"{hour:02d}:{minute}:{second}")