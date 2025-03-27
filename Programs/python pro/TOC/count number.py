# AIM : Design a machine program for creating a machine which count number of 0's & 1's in a given string.

def count_zeros_ones(input_string):
    count_zeros = input_string.count('0')
    count_ones = input_string.count('1')
    return count_zeros, count_ones

test_strings = [
    "110010",  
    "101010",  
    "111",     
    "00000",   
]

for test_str in test_strings:
    zeros, ones = count_zeros_ones(test_str)
    print(f"String '{test_str}' has {zeros} zeros and {ones} ones.")
