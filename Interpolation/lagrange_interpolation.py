from IPython.display import display
import numpy as np
import sympy as sp

def lagrange(f, values, degree = 10):
    p = 0
    x = sp.symbols('x')

    for i in range(degree):
        temp = 1
        for j in range(degree):
            if j == i:
                continue
            
            temp *= (x - values[j]) / (values[i] - values[j])
        
        p += temp * f[i]

    return p

def main():
    x, i = sp.symbols('x i')
    values = [0, 1, 2, 3]
    f = [1, 2, 9, 28]

    res = lagrange(f, values, 3)
    display(res)
    

if __name__ == '__main__':
    main()