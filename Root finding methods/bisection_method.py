import matplotlib.pyplot as plt
import numpy as np

def bisection_method(f, low, high, max_error):
    error_log = []

    while high - low > max_error:
        mid = low + (high - low) / 2

        if np.sign(f(mid)) * np.sign(f(high)) < 0:
            low = mid
        else:
            high = mid

        error_log.append(high - low)

    return low + (high - low) / 2, error_log

def main():
    f = lambda x: np.exp(x) - 2
    bisection_error_function = lambda x: 1 / (2 ** x)
    points = np.arange(20)

    sol, errors = bisection_method(f, -10, 10, 1e-6)
    
    print(f'Solution of the funtion is: {sol}')

    fig, ax = plt.subplots(2)
    fig.suptitle('Bisection Error')
    fig.tight_layout(pad=2.0)
    ax[0].plot(errors)
    ax[0].set_title('Simulation error', loc='right')
    ax[1].plot([bisection_error_function(point) for point in points])
    ax[1].set_title('Real error', loc='right')
    plt.show()


if __name__ == '__main__':
    main()