import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_rule(f, h, t, s0):
    n = len(t)
    s = np.zeros(n)
    s[0] = s0

    for i in range(n - 1):
        s[i + 1] = s[i] + h * f(t[i] + h / 2, s[i] + (h / 2) * f(t[i], s[i]))
    
    return s

def plot(t, s, F, h, i, axs):
    i -= 1
    idx = ((i % 3), (i % 2))
    axs[idx].plot(t, s, 'b', label='Approximation')
    axs[idx].plot(t, F(t), 'g', label='Real')
    axs[idx].set_title(f'h = {h}')
    axs[idx].grid()

def main():
    f = lambda t, s: np.exp(-t)
    F = lambda t: -np.exp(-t)

    fig, axs = plt.subplots(3, 2)
    for i in range(1, 7):
        h = 1/2**i
        t = np.linspace(0, 1, int(1/h) + 1)

        s = trapezoidal_rule(f, h, t, -1)

        plot(t, s, F, h, i, axs)
    
    for ax in axs.flat:
        ax.set(xlabel='t', ylabel='f(t)')
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()