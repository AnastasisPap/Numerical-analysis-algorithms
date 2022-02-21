import numpy as np


def partialPivoting(matrix, row):
    n, m = np.shape(matrix)
    maxPivot = abs(matrix[row][row])
    maxPos = row

    for i in range(row + 1, n):
        if abs(matrix[i][row]) > maxPivot:
            maxPivot = abs(matrix[i][row])
            maxPos = i

    matrix[[row, maxPos]] = matrix[[maxPos, row]]
    
    return matrix

def completePivoting(matrix, P, row):
    maxPivot = abs(matrix[row][row])
    maxPos = (row, row)
    n, m = np.shape(matrix)
    

    for i in range(row + 1, n):
        for j in range(row + 1, n):
            if abs(matrix[i][j]) > maxPivot:
                maxPivot = abs(matrix[i][j])
                maxPos = (i, j)
    
    n, m = maxPos
    matrix[:, [row, m]] = matrix[:, [m, row]]
    P[:, [row, m]] = P[:, [m, row]]
    matrix[[row, n]] = matrix[[n, row]]

    return P, matrix