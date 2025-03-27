# AIM : Design a program for creating machine that accpets the sting always ending with 101.

def is_accepted(input_string):
    state = 'q0'

    for symbol in input_string:
        if state == 'q0':
            if symbol == '1':
                state = 'q1'
        elif state == 'q1':
            if symbol == '0':
                state = 'q2'
            elif symbol == '1':
                state = 'q1'
        elif state == 'q2':
            if symbol == '1':
                state = 'q_accept'
            elif symbol == '0':
                state = 'q0'
        elif state == 'q_accept':
            break

    return state == 'q_accept'

test_strings = [
    "101",      
    "1101",     
    "01101",    
    "1",      
    "1001",   
    "100101",   
    "111101", 
]

for test_str in test_strings:
    result = is_accepted(test_str)
    print(f"String '{test_str}' is {'accepted' if result else 'rejected'}")
