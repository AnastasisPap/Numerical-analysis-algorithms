import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def simpson_three_eights(f, interval, h):
    x = sp.symbols('x')
    x0, x3n = interval

    res = f.subs(x, x0) + f.subs(x, x3n)
    xi = x0 + h
    part1 = 0
    part2 = 0
    i = 1

    while xi < x3n:
        if i % 3 == 0:
            part2 += f.subs(x, xi)
        else:
            part1 += f.subs(x, xi)
        i += 1
        xi += h
    
    res += 3 * part1 + 2 * part2
    return res * 3 * h / 8


def main():
    x = sp.symbols('x')
    f = x**4
    interval = [0, 1]
    real = sp.integrate(f, (x, interval[0], interval[1]))
    errors = []
    h = []


    for i in range(1, 4 + 1):
        res = simpson_three_eights(f, interval, 1/3**i)
        h.append(3**i)
        print(res)
        error = abs(real - res)
        print(f'Error: {error}')
        errors.append(error)

    plt.title('Simpson 3/8 rule error')
    plt.plot(h, errors, color='b')
    plt.xlabel('Number of points')
    plt.ylabel('Error')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()