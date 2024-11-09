import numpy as np
import matplotlib.pyplot as plt

def bisection(a, b, dx, fx):
    a1 = 0
    b1 = 0
    xs = 0
    counter = 0
    fig, ax = plt.subplots(figsize=(8, 6))

    while b1-a>dx:
        xs = (a+b1)/2
        if fx(a) * fx(xs) < 0:
            b1 = xs
            counter+=1
        else:
            a = xs
            counter+=1
    ax.plot(xs, fx(xs), 'ro', markersize=5)


    while b-a1>dx:
        xs = (a1+b)/2
        if fx(a1) * fx(xs) < 0:
            b = xs
            counter+=1
        else:
            a1 = xs
            counter+=1
    ax.plot(xs, fx(xs), 'ro', markersize=5)

    print("Perfect root:", xs)
    print("Count complete iterations: ", counter)
    x = np.arange(a, b, dx)
    y = fx(x)

    
    ax.plot(x, y, color='blue', linewidth=1)

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

# a = -2.0
# b = 2.5
# dx = 0.01

# bisection(a, b, dx)