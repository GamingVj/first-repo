# Program 2 B find sum of diagonals
# A simple Python program to # find sum of diagonals

MAX = 100 
def printDiagonalSums(mat, n):
    prinicipal = 0
    secondary = 0;
    for i in range(n):
        for j in range(n):

            # Condition for principal diagonal
            if(i == j):
                prinicipal += mat[i][j]
            
            # Condition for secondary diagonal
                if (i + j) == (n - 1):
                    secondary += mat [i][j]

    print("Principal Diagonal:", prinicipal)
    print("Secondary Diagonal:", secondary)