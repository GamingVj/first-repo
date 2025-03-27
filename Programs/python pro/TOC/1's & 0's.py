# AIM : Design a program for creating a machine which accepts string having even no. of 1's & 0's.

def is_accepted(input_string):
    count_ones = input_string.count('1')
    count_zeros = input_string.count('0')
    return count_ones % 2 == 0 and count_zeros % 2 == 0

test_strings = [
    "1100",     
    "1010",     
    "111000",   
    "1001",     
    "110",      
]

for test_str in test_strings:
    result = is_accepted(test_str)
    print(f"String '{test_str}' is {'accepted' if result else 'rejected'}")
