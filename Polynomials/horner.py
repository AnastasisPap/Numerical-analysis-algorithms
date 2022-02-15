import numpy as np
import sympy as sp

def horner(array, x0):
    res = array[0]

    for i in range(1, len(array)):
        res = res * x0 + array[i]
    
    return res


def main():
    x = sp.symbols('x')
    p = 3 * x**5 - 2 * x ** 3 + x
    degree = 5
    coeffs = []
    while degree >= 0:
        coeffs.append(p.coeff(x, degree))
        degree -= 1
    print(coeffs)
    x0 = -2

    print(horner(coeffs, -1*x0))


if __name__ == '__main__':
    main()