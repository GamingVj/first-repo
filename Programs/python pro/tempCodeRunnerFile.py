"""# It is used to find if the given number is prime or no

number = int(input("Enter a number.\n-->"))

if number < 2:
    print(f"{number} is not prime number")

else:
    is_prime = True

for i in range(2, (int(number**0.5))+1):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{number} is prime")

else:
    print(f"{number} is not prime")
"""
# a = int(input("Enter a the 1st Number:\n-->"))
# b = int(input("Enter the 2nd Number:\n-->"))
#
# sum = a + b
#
# print({a}, '+', {b}, "is equal to", [sum],)

# a = int(input("Enter a the 1st Number:\n-->"))
# b = int(input("Enter the 2nd Number:\n-->"))
#
# if a > b:
#     print({a}, "is Greater than", {b})
# else:
#     print({b}, "is Greater than", {a})
#

# i = 1
# while True:
#     if i%3 == 0:
#         break 
#     print(i)

#     i += 1

import re
sentence = 'we are humans'
matched = re.match(r'(,*) (.*?) (.*)', sentence)
if matched:
    print(matched.groups())
