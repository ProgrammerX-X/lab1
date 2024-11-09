import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def methodNewtons(x, fx):
    e = 0.01
    e1 = 1
    xf = sp.symbols('x')
    counter = 0
    fig, ax = plt.subplots(figsize=(7, 5))

    while e1 > e:
        x1 = x
        f_value = float(fx(x))
        derivative_value = float(sp.diff(fx(xf), xf).subs(xf, x))
        x = x - f_value / derivative_value
        e1 = abs(x - x1)
        counter+=1

    print(f"Perfect root: {x}")
    print(f"Count complete iterations: {counter}")

    x_plot = np.linspace(-2.5, 2.5, 400)
    y_plot = [float(fx(xi).evalf()) for xi in x_plot]

    ax.plot(x_plot, y_plot, 
            color='blue', linewidth=1)

    ax.set_xlim(-2.7, 2.7)
    ax.set_ylim(-2.7, 2.7)

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    ax.grid(True, linestyle='--', alpha=0.7)

    ax.set_xlabel('X', fontsize=14)
    ax.set_ylabel('Y', fontsize=14)

    ax.set_title('Графік функції $f(x)$', fontsize=16)

    ax.legend(loc='best')

    plt.show()

# x_initial = -2.5

# methodNewtons(x_initial)
