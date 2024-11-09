'''
    a) Enter on r by c matrix M(r and c being positive integers).
    b) Display M in matrix format.
    c) Display the row and columns of M for Matrix M-printing rows.
    d) Find the scalar multiplication of M for a given scalar.
    e) Find the transpose of the matrix M.
'''

 # a) Enter on r by c matrix M(r and c being positive integers).
 
import numpy as np

A = np.array(  [[1,1,2],
                [2,6,7],
                [3,6,7]])
print(A)


# b) Display M in matrix format.

B = np.array ( [[1,1,2],
                [2,6,7],
                [3,6,7]])
print(B)


# c) Display the row and columns of M for Matrix M-printing rows.

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Display rows
print("Rows:")
for row in M:
    print(row)

# Display columns
print("Columns:")
for col in range(len(M[0])):
    column = [row[col] for row in M]
    print(column)


# d) Find the scalar multiplication of M for a given scalar.

a = 5

M = np.array([[5,5,10],
              [10,40,35],
              [15,30,35]])
print(M)


# e) Find the transpose of the matrix M.

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_M = transpose(M)
print("Original Matrix:")
for row in M:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_M:
    print(row)