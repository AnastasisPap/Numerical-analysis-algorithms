import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def secant(f, x0, x1, max_error):
    x = sp.symbols('x')
    errors = []
    error = float('inf')

    while error > max_error:
        if f.subs(x, x0) == f.subs(x, x1):
            return None, None
        
        x2 = np.float64(x0) - np.float64((x1 - x0) * f.subs(x, x0)) / np.float64((f.subs(x, x1) - f.subs(x, x0)))
        x0 = x1
        x1 = x2

        error = abs(f.subs(x, x2))
        errors.append(abs(error - f.subs(x, x0)))

    return x2, errors


def main():
    x = sp.symbols('x')
    f = x**3 - 5*x + 3
    
    sol, errors = secant(f, 0, 1, 1e-6)

    if sol is None:
        print('No solution')
    else:
        print(f'Solution of the function is: {sol}')

        plt.title('Secant method')
        plt.plot(errors)
        plt.show()


if __name__ == '__main__':
    main()