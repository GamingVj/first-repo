# AIM : Design a program to find 2's complement of a given binary number.

def twos_complement(binary_str):
    n = len(binary_str)
    ones_complement = ''.join('1' if bit == '0' else '0' for bit in binary_str)
    twos_complement = bin(int(ones_complement, 2) + 1)[2:].zfill(n)
    return twos_complement

binary_str = "1101"
print(f"2's complement of {binary_str} is {twos_complement(binary_str)}")
