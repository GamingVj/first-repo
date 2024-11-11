''' 
    Write a program to enter a matrix and check if it is invertible . 
    If the inverse exists, find the inverst.
'''
import numpy as np

def is_invertible(matrix):
    return np.linalg.det(matrix) != 0

def find_inverse(matrix):
    return np.linalg.inv(matrix)

def main():
    # Predefined matrix
    matrix = np.array([
        [1, 2, 3],
        [0, 1, 4],
        [5, 6, 0]
    ])

    print("Matrix:")
    print(matrix)

    # Check if the matrix is invertible
    if is_invertible(matrix):
        print("The matrix is invertible.")
        inverse_matrix = find_inverse(matrix)
        print("The inverse of the matrix is:")
        print(inverse_matrix)
    else:
        print("The matrix is not invertible.")

if __name__ == "__main__":
    main()