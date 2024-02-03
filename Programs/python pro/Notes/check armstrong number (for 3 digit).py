# take input from user
num = int(input("Enter a Number:\n-->"))

# initialize sum
sum = 0

# Find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp //= 10

# Display the result
if num == sum:
    print(num, "is an Armstrong Number")
else:
    print(num, "is an not Armstrong Number")
