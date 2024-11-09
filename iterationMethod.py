# 1. Ми вибираємо наший інтервал (а, б)
# 2. Далі вибираємо крок (наприклад 0.01)
# Принцип роботи методу ітерації:
# 1. Ми від першої межі до другої крокуємо із кроком 0.01(бажаний крок)
# крок вираховуємо так: dx = b-a/n(кількість розбиттів)
# умова: якщо f(xi)*f(xi+dx) < 0
# тоді: x = (xi + (xi+dx))/2
# break
# else:
# dx = b-a/n

# import math
import matplotlib.pyplot as plt
import numpy as np

def iterationMethodFunc(a, b, dx, fx):
    
    x = 0.0
    count = 0

    n = (b-a)/dx
    i = a
    fig, ax = plt.subplots(figsize=(7, 5))
    while i<b:
        if fx(i)*fx(i+dx) < 0 :
            x = (i + (i+dx))/2
            count+=1
            ax.plot(x, fx(x), 'ro', markersize=5)
            i+=dx
            break
        else:
            i+=dx
            count+=1
    print("Perfect root: ", x)
    print("Count possible iterations: ", n)
    print("Count complete iterations: ", count)
    
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
    


# a = -2.5
# b = 2.5
# dx = 0.0001

# iterationMethodFunc(a, b, dx)
