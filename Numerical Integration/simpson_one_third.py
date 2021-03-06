import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def simpson_one_third(f, interval, h):
    x = sp.symbols('x')
    x0, x2n = interval

    res = f.subs(x, x0) + f.subs(x, x2n)
    part1 = 0
    part2 = 0
    xi = x0 + h
    i = 0

    while xi < x2n:
        if i % 2 == 0:
            part1 += f.subs(x, xi)
        else:
            part2 += f.subs(x, xi)

        i += 1
        xi += h
    
    res += 4 * part1 + 2 * part2
    
    return res * h / 3


def main():
    x = sp.symbols('x')
    f = x**4
    interval = [0, 1]
    real = sp.integrate(f, (x, interval[0], interval[1]))
    errors = []
    h = []


    for i in range(2, 7 + 1):
        res = simpson_one_third(f, interval, 1/2**i)
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