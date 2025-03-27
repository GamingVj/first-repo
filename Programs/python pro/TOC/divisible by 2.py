# AIM : Design a program for accepting binary number divisible by 2.

def is_accepted(input_string):
    return input_string[-1] == '0'

test_strings = [
    "0",
    "1",
    "10",
    "110",
    "101",
    "1001",
]

for test_str in test_strings:
    result = is_accepted(test_str)
    print(f"String '{test_str}' is {'accepted' if result else 'rejected'}")
