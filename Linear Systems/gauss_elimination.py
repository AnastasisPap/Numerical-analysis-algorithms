from functools import partial
from random import gauss
import numpy as np
from pivoting_methods import *


# pivotMethod:
# 0 = normal elimination
# 1 = partial pivoting
# 2 = weighted partial pivoting
# 3 = full pivoting
def gauss_elimination(matrix, pivotMethod = 0):
    n, m = np.shape(matrix)

    if n + 1 != m:
        print('Invalid matrix')
        return

    P = np.eye(n)

    for row in range(n):
        if pivotMethod == 1:
            matrix = partialPivoting(matrix, row)
        elif pivotMethod == 2:
            P, matrix = completePivoting(matrix, P, row)

        if matrix[row][row] == 0:
            print('Dividing with 0')
            return

        for i in range(row + 1, n):
            c = matrix[i][row] / matrix[row][row]
            
            for j in range(row, m):
                matrix[i][j] -= c * matrix[row][j]
        
        matrix[row] = matrix[row] / matrix[row][row]

    return matrix, P

def solve_matrix(matrix):
    n, m = np.shape(matrix)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][-1]

        for j in range(n - 1, i, -1):
            x[i] -= matrix[i][j] * x[j]

    return x

def main():
    matrix = np.array([
        [1, -2, 1, 0],
        [2, 1, -3, 5],
        [4, -7, 1, -1]
        ], np.float32)

    for i in range(3):
        matrix, P = gauss_elimination(matrix, i)
    
        print(np.dot(P, solve_matrix(matrix)))


if __name__ == '__main__':
    main()