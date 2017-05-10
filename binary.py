def int_to_bin(n):
    if (n == 0):
        return 0
    bits = []
    while (n > 0):
        bits.append(n % 2)
        n = n // 2
    return bits

print(str(int_to_bin(13)))
