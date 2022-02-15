import numpy as np
import sympy as sp


def aitken(p):
    return [p[i+2] - np.power(p[i+1] - p[i], 2) / (p[i + 2] - 2 * p[i + 1] + p[i]) for i in range(len(p) - 2)]


def steffensen(f, xn, max_iter):
    x = sp.symbols('x')
    p0 = xn
    p1 = f.subs(x, p0)
    p2 = f.subs(x, p1)

    for i in range(max_iter):
        p0 = p2 - np.power(p1 - p0, 2) / (p2 - 2 * p1 + p0)
        p1 = f(p0)
        p2 = f(p1)

    return p2