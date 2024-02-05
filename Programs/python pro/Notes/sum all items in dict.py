a = int(input("Enter the first number:\n-->"))
b = int(input("Enter the second number:\n-->"))
c = int(input("Enter the third number:\n-->"))

# Function to print sum
def returnSum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i

    return sum

# Driver Function
dict = {'a': a,'b': b,'c': c}
print("Sum :",returnSum(dict))