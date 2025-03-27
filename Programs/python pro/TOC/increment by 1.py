# AIM : Design a program which will increment the given binary number by 1.

def increment_binary(binary_str):
    return bin(int(binary_str, 2) + 1)[2:]

binary_str = "1101"
print(f"Incremented binary of {binary_str} is {increment_binary(binary_str)}")
