import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def simulate(f, interval, iterations):
    x = sp.symbols('x')
    iter = 0
    a, b = interval
    s = 0

    while iter < iterations:
        xi = np.random.uniform(a, b)
        s += f.subs(x, xi)
        iter += 1

    return ((b - a) / iterations ) * s


def main():
    x = sp.symbols('x')
    f = x**4

    interval = [0, 1]
    real = sp.integrate(f, (x, interval[0], interval[1]))
    errors = []
    iterations = []

    for i in range(2, 6):
        res = simulate(f, interval, 10**i)
        iterations.append(10**i)
        error = abs(res - real)
        print(res)
        print(f'Error: {error}')
        errors.append(error)
    
    plt.title('Monte Carlo Simulation for Numerical Integration')
    plt.plot(iterations, errors, color='b')
    plt.xlabel('Iterations')
    plt.ylabel('Error')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()