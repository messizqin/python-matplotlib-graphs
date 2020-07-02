from matplotlib import pyplot as plt
from math import sin, cos, radians
import numpy as np

sup_2 = '\N{SUPERSCRIPT TWO}'


def force(theta):
    m = 50
    g = 9.8
    f_press = 350
    return 0.2 * m * g * sin(radians(theta)) * sin(radians(theta)) + f_press * cos(radians(90 - theta))


x = np.linspace(45, 90, 100)
y = []
for i in x:
    y.append(force(i))

plt.title('By pedaling on the starting block with same force\n'
          'how much forward force (parallel to the ground) I can get\n'
          'by setting starting block to different angles?', fontsize=14)
plt.xlabel('degree of starting block (degree)', fontsize=14)
plt.ylabel('parallel force pointing forward\n(Newton)', fontsize=14)
plt.plot(x, y, label=f'F = 20%mg sin{sup_2}\u03b8 + Fp cos(90 - \u03b8)', color='k')

dx = [45, 60, 70, 80, 90]
dy = []
for i in dx:
    di = force(i)
    dy.append(di)
    if i == 45:
        plt.annotate(s=f'({i}, {round(di)})', xy=[i + 6, di + 20], fontsize=14)
    elif i != 90 and i != 80:
        plt.annotate(s=f'({i}, {round(di)})', xy=[i + 2, di], fontsize=14)
    elif i == 80:
        plt.annotate(s=f'({i}, {round(di)})', xy=[i - 8, di + 4], fontsize=14)
    else:
        plt.annotate(s=f'({i}, {round(di)})', xy=[i - 7, di - 14], fontsize=14)

plt.scatter(dx, dy, color='k', linewidths=3)
plt.legend(fontsize=14, loc='lower right')
plt.tight_layout()
plt.show()


