"""
    Function to print sum
------------------------------------
defining a  function name (dict)
"""


def return_sum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i

    return sum


'''
            Driver Function
------------------------------------
Getting the values of a, b and c from user as an input vvv
'''

a = int(input("Enter the 1st value out of 3\n-->"))
b = int(input("Enter the 2nd value out of 3\n-->"))
c = int(input("Enter the 3rd value out of 3\n-->"))

# creating a dictionary with  key value pairs

mydict = {'a': a, 'b': b, 'c': c}
print("Sum :", return_sum(mydict))
