from urllib.parse import ParseResultBytes
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

    res = complex_trapezoid(f, interval, 1/4)
    real = sp.integrate(f, (x, interval[0], interval[1]))
    print(res)
    print(f'Error: {abs(real - res)}')


if __name__ == '__main__':
    main()