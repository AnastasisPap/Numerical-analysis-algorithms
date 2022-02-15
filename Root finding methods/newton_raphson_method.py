from typing import NewType
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def NewtonRaphson(f, df, xi, max_error):
    x = sp.symbols('x')
    errors = []
    prev = 0

    while f.subs(x, xi) > max_error:
        if df.subs(x, xi) == 0:
            return None, None
        
        errors.append(abs(f.subs(x, xi) - f.subs(x, prev)))
        prev = xi
        xi = xi - np.float64(f.subs(x, xi)) / np.float64(df.subs(x, xi))

    return xi, errors


def main():
    x = sp.symbols('x')
    f = x**3 - 5*x + 3
    df = f.diff(x)

    sol, errors = NewtonRaphson(f, df, 2, 1e-6)

    if sol is None:
        print('No solution')
    else:
        print(f'Solution of the function is: {sol}')

        plt.title('Newton-Raphson method')
        plt.plot(errors)
        plt.show()


if __name__ == '__main__':
    main()