# AIM : Design a program for Mode 3 Machine.

def is_accepted(input_string):
    count_ones = 0
    for symbol in input_string:
        if symbol == '1':
            count_ones += 1
    return count_ones == 3

test_strings = [
    "111",      
    "10101",    
    "1101",     
    "1001",     
    "11111",    
]

for test_str in test_strings:
    result = is_accepted(test_str)
    print(f"String '{test_str}' is {'accepted' if result else 'rejected'}")
