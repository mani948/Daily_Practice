def sumXor(n):
    if n == 0:
        return 1

    zero_bits = 0

    while n > 0:
        if (n & 1) == 0:
            zero_bits += 1
        n >>= 1

    return 1 << zero_bits


n=int(input())
print(sumXor(n))