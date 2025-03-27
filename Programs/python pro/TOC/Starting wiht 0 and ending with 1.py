# AIM : Design a DFA over the input set {0,1} accept all the strings starting with 0 & ending with 1

def is_accepted(input_string):

    return input_string.startswith('0') and input_string.endswith('1')

test_strings = [
    "01",        
    "001",       
    "011",       
    "1",         
    "10",        
    "100",       
    "1101",      
]

for test_str in test_strings:
    result = is_accepted(test_str)
    print(f"String '{test_str}' is {'accepted' if result else 'rejected'}")
