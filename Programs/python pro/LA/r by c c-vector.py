'''
  Write a program to do the following:
  a) Find the vector matrix multipication of a r by c matix an c-vector u.
  b) Find the matirx matrix priduct of M  with a c by p matix N.
'''

# a) Find the vector matrix multipication of a r by c matix an c-vector u.

import numpy as np
a = np.array([0,4,6])
b= np.array([[1,2],[4,9],[-1,-10]])
print(np.dot(a,b))

# b) Find the matirx matrix priduct of M  with a c by p matix N.
def matrix_multiply(M, N):
    # Get the dimensions of the matrices
    r = len(M)
    c = len(M[0])
    p = len(N[0])

    # Check if the number of columns in M is equal to the number of rows in N
    if c != len(N):
        raise ValueError("Number of columns in M must be equal to the number of rows in N")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(p)] for _ in range(r)]

    # Perform matrix multiplication
    for i in range(r):
        for j in range(p):
            for k in range(c):
                result[i][j] += M[i][k] * N[k][j]

    return result

# Example usage
M = [
    [1, 2, 3],
    [4, 5, 6]
]

N = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = matrix_multiply(M, N)
print("Matrix M:")
for row in M:
    print(row)

print("\nMatrix N:")
for row in N:
    print(row)

print("\nMatrix product of M and N:")
for row in result:
    print(row)