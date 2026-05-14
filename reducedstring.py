s = input()

result = []

for ch in s:
    if result and result[-1] == ch:
        result.pop()   # remove adjacent matching character
    else:
        result.append(ch)

final_string = "".join(result)

if final_string == "":
    print("Empty String")
else:
    print(final_string)