import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def simple_trapezoid(f, points):
    x0, x1 = points
    x = sp.symbols('x')
    f0 = f.subs(x, x0)
    f1 = f.subs(x, x1)
    h = x1 - x0

    return h * (f0 + f1) / 2


def complex_trapezoid(f, interval, h):
    x = sp.symbols('x')
    x0, xn = interval

    temp = 1/2 * (f.subs(x, x0) + f.subs(x, xn)) 
    xi = x0 + h
    while xi < xn:
        temp += f.subs(x, xi)
        xi += h

    return h * temp


def main():
    x = sp.symbols('x')
    f = x**4
    interval = [0, 1]
    real = sp.integrate(f, (x, interval[0], interval[1]))
    errors = []
    h = []

    for i in range(7 + 1):
        res = complex_trapezoid(f, interval, 1/2**i)
        h.append(2**i)
        #print(res)
        error = abs(real - res)
        #print(f'Error: {error}')
        errors.append(error)   

    plt.title('Trapezoidal rule error')
    plt.plot(h, errors, color='b')
    plt.xlabel('Number of points')
    plt.ylabel('Error')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()