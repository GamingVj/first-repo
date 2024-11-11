'''
    Write a program to convert a matrix into its now echelon form.
'''

import numpy as np

def row_echelon_form(matrix):
    matrix = matrix.astype(float)  # Ensure the matrix is of type float for division
    rows, cols = matrix.shape

    for i in range(min(rows, cols)):
        # Find the pivot row
        max_row = i + np.argmax(np.abs(matrix[i:, i]))
        if matrix[max_row, i] == 0:
            continue  # Skip if the pivot is zero

        # Swap the current row with the pivot row
        matrix[[i, max_row]] = matrix[[max_row, i]]

        # Normalize the pivot row
        matrix[i] = matrix[i] / matrix[i, i]

        # Eliminate the entries below the pivot
        for j in range(i + 1, rows):
            matrix[j] = matrix[j] - matrix[j, i] * matrix[i]

    return matrix

# Predefined matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Original Matrix:")
print(matrix)

echelon_matrix = row_echelon_form(matrix)
print("\nRow Echelon Form:")
print(echelon_matrix)