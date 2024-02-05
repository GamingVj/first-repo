def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the function
n = int(input("Enter the number of terms:\n-->"))

print(f"The {n}th Fibonacci number is {fibonacci(n)}")