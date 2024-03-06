from builtins import input
# PROGRAM 2A: row-sum, COLUMN-wise of 2D array ARRAY
# Program 2 A row-sum & COLUMN-wise Sum of 2D ARRAY

n = int(input("Enter the number of rows:"))
m = int(input("Enter the number of columns:"))
matrix = []
print("Enter values in matrix")
# for user input 
for i in range(n):
    data = []
    for j in range(m):
        data.append(int(input()))
    matrix.append(data)

# For printing the matrix
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end =" ")
    print()

# For printing row wise sum
for i in range(n):
    sum = 0
    for j in range(m):
        sum = sum + matrix[i][j]
    print('Sum of row', i+1, ':', sum)

# For printing column wise sum
for i in range(m):
    sum = 0
    for j in range(n):
        sum = sum + matrix[j][i]
    print('Sum of column', i+1, ':', sum)
