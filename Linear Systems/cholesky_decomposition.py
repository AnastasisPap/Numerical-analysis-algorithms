import numpy as np


def cholesky(matrix):
    n, m = np.shape(matrix)

    if n != m:
        print('Not a square matrix')
        return
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                print('The matrix is not symmetric')
    
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            temp_sum = sum([L[i][k] * L[j][k] for k in range(j)])
        
            if i == j:
                if matrix[i][i] - temp_sum < 0:
                    print('Matrix is not positively defined')
                    return
                
                L[i][i] = np.sqrt(matrix[i][i] - temp_sum)
            else:
                L[i][j] = (matrix[i][j] - temp_sum) / L[j][j]
    
    return L

def check_if_valid_L(matrix, L):
    A = np.dot(L, L.T)
    n, m = np.shape(matrix)

    for i in range(n):
        for j in range(n):
            if np.float32(A[i][j]) != np.float32(matrix[i][j]):
                return False

    return True

def main():
    matrix = np.array([
        [6, 15, 55],
        [15, 55, 225],
        [55, 225, 979]
    ])

    L = cholesky(matrix)
    print(L)
    print(check_if_valid_L(matrix, L))


if __name__ == '__main__':
    main()