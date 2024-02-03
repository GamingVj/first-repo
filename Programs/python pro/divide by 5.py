# It is used to check if the number is divisible by 5 or not

number = int(input("\nEnter a number\n-->"))

# condition  for checking if the number is divisible by 5 or not. If it is then print that
if number % 5 == 0:
    print(f"{number} is divisible by 5\n")
else:
    print(f"{number} is not divisible by 5\n")
