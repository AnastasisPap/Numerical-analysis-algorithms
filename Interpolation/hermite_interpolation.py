import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def Li(points, i):
    x = sp.symbols('x')
    res = 1

    for j in range(len(points) + 1):
        if i == j:
            continue
        res *= (x - points[j])
    
    temp = 1
    for j in range(len(points) + 1):
        if j == i:
            continue
        temp *= (points[i] - points[j])
    
    return res/temp

def Hi_1(points, i):
    x = sp.symbols('x')
    Li = Li(points, i)
    dLi = sp.diff(Li, x)
    dLxi = dLi.subs(x, points[i])

    return (1 - 2 * (x - points[i]) * dLxi) * sp.Pow(Li, 2)

def Hi_2(points, i):
    x = sp.symbols('x')
    Li = Li(points, i)

    return (x - points[i]) * sp.Pow(Li, 2)

def hermite(f, points):
    x = sp.symbols('x')
    p = 0
    df = sp.diff(f, x)

    for i in range(1, len(points)):
        p += f.subs(x, points[i]) * Hi_1(points, i) + df.subs(x, points[i]) * Hi_2()
    
    return p