from functools import partial
from pivoting_methods import *
import numpy as np


def get_permutation_matrix(n):
    P = np.zeros((n, n))
    for i in range(n):
        for j in range(n-1, -1, -1):
            if n - i - 1 == j:
                P[i][j] = 1
    
    return P

# pivotMethod:
# 0 = normal elimination
# 1 = partial pivoting
# 2 = full pivoting
def PLU(matrix, pivotMethod = 0):
    n, m = np.shape(matrix)

    if n != m:
        print('Not square matrix')
        return

    P = np.eye(n)
    L = np.eye(n)
    P1 = np.eye(n)
    cnt = 0
    U = np.zeros((n, m))

    for row in range(n):
        M = np.eye(n)
        if pivotMethod == 1:
            P1, matrix = partialPivoting(matrix, row, np.eye(n))
        elif pivotMethod == 2:
            P1, matrix = completePivoting(matrix, row, np.eye(n), L)
        
        if not np.array_equal(P, P1):
            cnt += 1
        P = np.dot(P1, P)
        
        if matrix[row][row] == 0:
            print('Dividing with 0')
            return None, None, None
        
        for i in range(row + 1, n):
            c = (matrix[i][row] / matrix[row][row])
            M[i][row] = -c
            L[i][row] = c

    
        matrix = np.dot(M, matrix)

    return P, L, matrix, cnt


def det(P, U, cnt):
    cnt = 0
    n, m = np.shape(P)

    diagonal_mul = 1
    for i in range(n):
        diagonal_mul *= U[i][i]

    return (-1) ** cnt * diagonal_mul

def main():
    matrix = np.array([
        [0, 1, 2],
        [2, -2, 1],
        [5, 3, 1]
    ])

    b = np.array([7, 9, 9]).T
    P, L, U, cnt = PLU(matrix, 1)
    print(f'Determinant: {det(P, U, cnt)}')


if __name__ == '__main__':
    main()