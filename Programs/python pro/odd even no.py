# \n is use to exec in new line
a = int(input("Enter the Starting Number\n-->"))
b = int(input("Enter the Ending Number\n-->"))

# TO print the text "EVEN NUMBER"
print("\nEVEN NUMBER\n")

# for printing output of even numbers -->
# if condition 
if a % 2 == 0:
    for ab in range(a, b, 2):
        print(ab)

# else condition
else:
    for ab in range(a-1, b, 2):
        print(ab)

# TO print the text "ODD NUMBER"
print("\nODD NUMBERS\n")

# for printing output of odd numbers -->
# if condition
if a % 2 == 0:
    # for condition for odd no.
    for i in range(a-1, b, 2):
        print(i)

# else condition
else:
    for j in range(a, b, 2):
        print(j)
        