import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def chebyschev(degree):
    x = sp.symbols('x')
    T0 = 1
    T1 = x
    Tn = 0

    for i in range(2, degree+1):
        Tn = 2 * x * T1 - T0
        T1 = Tn
        T0 = T1
    
    return Tn

def get_chebyschev_points(interval, degree):
    i = sp.symbols('i')
    a, b = interval
    point = sp.cos((2 * i - 1) * sp.pi / 2 * degree)
    return ((b + a) / 2) + ((b - a) / 2) * point

def main():
    x, i = sp.symbols('x i')
    interval = [3, 4]
    degree = 2

    x = get_chebyschev_points(interval, degree)
    points = [x.subs(i, k) for k in range(1, degree + 1)]
    p = chebyschev(degree)
    
    f = x ^ -3


if __name__ == '__main__':
    main()