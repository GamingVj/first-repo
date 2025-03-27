# AIM : Design a DFA over the input set {a,b} accept all the string starting with symbol a.

def is_accepted(input_string):
    if input_string and input_string[0] == 'a':
        return True
    return False

test_strings = [
    "a",        
    "ab",       
    "aabb",     
    "b",        
    "ba",       
    "bb",       
]

for test_str in test_strings:
    result = is_accepted(test_str)
    print(f"String '{test_str}' is {'accepted' if result else 'rejected'}")
