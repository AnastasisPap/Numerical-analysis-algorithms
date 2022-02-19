import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def forwardDifferences(f):
    res = []
    x = [i for i in f]

    for i in range(1, len(f)):
        for j in range(0, len(f) - i):
            x[j] = x[j+1] - x[j]
        
        res.append(x[:-1])

    return res


def newton_gregory(f, theta):
    diff = forwardDifferences(f)
    res = f[0]

    for i in range(1, len(diff) + 1):
        temp = 1
        for j in range(i):
            temp *= (theta - j) / (j + 1)
        
        res += diff[i-1][0] * temp

    return res

def main():
    points = [0, 1, 2, 3]
    f = [0, 4, 6, -6]
    x = sp.symbols('x')

    theta = (x - points[0]) / (points[1] - points[0])
    p = newton_gregory(f, theta).expand()
    interpolation_points = np.linspace(0, 3, 50, endpoint=True)
    p_y = [p.subs(x, point) for point in interpolation_points]

    plt.title('Newton-Gregory Interpolation')
    plt.plot(points, f,  'g', label='real values')
    plt.plot(interpolation_points, p_y, 'b', label='interpolation polynomial')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()