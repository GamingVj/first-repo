# This is a simple calculator program using def function in python.

# We define a function name opp which contains all the operator and there respective calculations.
def opp(a, b, op):
    if op == "+":
        return f"The addition of {a}+{b} is equal to {a + b}"
    elif op == "-":
        return f"The subtraction of {a}-{b} is equal to {a - b}"
    elif op == "*":
        return f"The multiplication of {a}x{b} is equal to {a * b}"
    elif op == "/":
        return f"The division of {a}/{b} is equal to {a / b}"
    else:
        print("Invalid operator")

# we define a function name total which contains all the operator sum and there respective calculations.
def total(a, b, op):
    if op == "+":
        print('Answer of the calculations using other operators are:-')
        return f'{a}-{b}={a-b},\n{a}*{b}={a*b},\n{a}/{b}={a/b}'
    elif op == "-":
        print('Answer of the calculations using other operators are:-')
        return f'{a}+{b}={a+b},\n{a}*{b}={a*b},\n{a}/{b}={a/b}'
    elif op == "*":
        print('Answer of the calculations using other operators are:-')
        return f'{a}+{b}={a+b},\n{a}-{b}={a-b},\n{a}/{b}={a/b}'
    elif op == "/":
        print('Answer of the calculations using other operators are:-')
        return f'{a}+{b}={a+b},\n{a}-{b}={a-b},\n{a}*{b}={a*b}'
    else:
        print("Invalid operator")


a = int(input("Enter the first number:\n-->"))
b = int(input("Enter the second number:\n-->"))
op = input("Enter the operator:\n-->")
print(opp(a, b, op))
print(total(a, b, op))
print("Thank you for using our calculator ☺")


