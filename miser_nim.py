def misereNim(s):
    xor_sum = 0
    all_ones = True

    for stones in s:
        xor_sum ^= stones
        if stones != 1:
            all_ones = False

    if all_ones:
        if len(s) % 2 == 0:
            return "First"
        else:
            return "Second"

    if xor_sum == 0:
        return "Second"
    else:
        return "First"


t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    print(misereNim(s))