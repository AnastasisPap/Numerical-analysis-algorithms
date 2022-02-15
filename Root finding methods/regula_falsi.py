import numpy as np
import matplotlib.pyplot as plt

def regula_falsi(f, low, high, max_error):
    error_log = []

    while high - low > max_error:
        mid = (low * f(high) - high * f(low)) / (f(high) - f(low))

        if np.sign(f(low)) * np.sign(f(mid)) < 0:
            high = mid
        else:
            low = mid
        
        print(high - low)
        
        error_log.append(high - low)

    return (low * f(high) - high * f(low)) / (f(high) - f(low)), error_log


def main():
    f = lambda x: x ** 3 - 2 * x + 2

    sol, errors = regula_falsi(f, -2, 2, 1e-6)

    print(f'Solution of the function is: {sol}')

    plt.title('Regula Falsi')
    plt.plot(errors)
    plt.show()


if __name__ == '__main__':
    main()