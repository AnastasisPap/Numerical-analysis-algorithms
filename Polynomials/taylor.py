from IPython.display import display
import numpy as np
import sympy as sp


def taylor(f, df, x0, degree=50):
    x = sp.symbols('x')
    res = 1
    num = 1

    if degree == 0:
        return f.subs(x, x0)
    
    df = df.diff(x)
    curr_item = ( df.subs(x, x0) / sp.factorial(degree) ) * ((x - x0) ** degree)

    return curr_item + taylor(f, df, x0, degree - 1)


def main():
    x = sp.symbols('x')
    f = 1/x

    p = taylor(f, f, 0, 3)
    display(p)

if __name__ == '__main__':
    main()