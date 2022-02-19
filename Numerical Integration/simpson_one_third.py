import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


def simple_simpson(f, interval):
    x = sp.symbols('x')
    x2, x0 = interval
    h = (x2 - x0) / 2

    return (h / 3) * (f.subs(x, x0) + 4 * f.subs(x, x0 + h), f.subs(x, x2))


def complex_simpson(f, interval, h):
    x = sp.symbols('x')
    x0, x2n = interval

    res = f.subs(x, x0) + f.subs(x, x2n)
    xi = x0 + h
    i = 0

    while xi < x2n:
        res += f.subs(x, xi) * (4 if i % 2 == 0 else 2)
        i += 1
        xi += h
    
    return res * h / 3


def main():
    x = sp.symbols('x')
    f = x**4
    interval = [0, 1]
    real = sp.integrate(f, (x, interval[0], interval[1]))
    errors = []
    h = []


    for i in range(2, 7 + 1):
        res = complex_simpson(f, interval, 1/2**i)
        h.append(2**i)
        print(res)
        error = abs(real - res)
        print(f'Error: {error}')
        errors.append(error)

    plt.title('Simpson 1/3 rule error')
    plt.plot(h, errors, color='b')
    plt.xlabel('Number of points')
    plt.ylabel('Error')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()