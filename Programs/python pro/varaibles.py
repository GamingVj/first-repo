"""
fruits = ['Vijay', 'Jay', 'Harsh']
x, y, z = fruits

print(x)
print(y)
print(z)

x = y = z = "Vijay"

print(x)
print(y)
print(z)

a = "hello World"
print(a[1])

for x in "banana":
    print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("screen" in txt)

a = input("Enter a String\n-->")
if "free" in a:
    print("Yes,'free' is present in",a)

txt = "The best things in life are free!"
print("free" not in txt)

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = " Hello, World! "
print(a.strip())

a = " Hello, World! "
print(a.replace("H", "J"))

a = "Hello, World ,!"
print(a.split(","))

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)


def swapPosition(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


List = [23, 65, 19, 90]
pos1, pos2 = 2, 4

print(swapPosition(List, pos1-2, pos2-1))

# functions to find the sum of all items in dictionary
def sum_of_values(dictionary):
    return sum(dictionary.values())

# Example dictionary
my_dict = {'a': 10, 'b': 20,'c': 30,'d': 40}

# Calculate the sum of values in the dictionary
result = sum_of_values(my_dict)

# Display the result
print(f'The sum of all values in the dictionary is : {result}')

# functions to find the sum of all items in dictionary
def sum_of_dict_items(dictionary):
    # Use the sum function to add up all the values in the dictionary
    total_sum = sum(dictionary.values())
    return total_sum
"""

'''
# Example dictionary
example_dict = {'a': 10, 'b': 20,'c': 30}

# Calculate the sum of values in the dictionary
result = sum_of_dict_items(example_dict)

# Display the result
print(f"Sum of all items in the dictionary:", result)
'''

'''
# Function to print sum
def returnSum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i

    return sum

# Driver Function
dict = {'a': 100,'b': 200,'c': 300}
print("Sum :",returnSum(dict))

'''

'''
import numpy as np
def returnSum(dict):
    values = np.array(list(dict.values()))
    return np.sum(values)

dict = {'a': 100,'b': 200,'c': 300}
print("Sum :", returnSum(dict))
'''
