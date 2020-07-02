from matplotlib import pyplot as plt
from math import cos, radians
import numpy as np


def force(u, m, g, theta):
    if isinstance(theta, int):
        return float((u * m * g) / cos(radians(theta)))
    else:
        res = []
        for i in theta:
            res.append(float((u * m * g) / cos(radians(i))))
        return res


x = np.linspace(20, 80, 1000)
y = force(0.5, 50, 9.8, x)

plt.style.use('seaborn-white')
plt.grid()
plt.title('Mass of a 50kg Athlete \nRunning on a track with a frictional coefficient of 0.5')
plt.xlabel('degree between the ground and power supply leg (Degree)', fontsize=14)
plt.ylabel('forced needed by power leg\nto surmount friction (Newton)', fontsize=14)

start_x = 30
start_y = force(0.5, 50, 9.8, 30)
end_x = 60
end_y = force(0.5, 50, 9.8, 60)
plt.fill_between([start_x, end_x], [start_y, start_y], [end_y, end_y], color='r', alpha=0.5, label='Start angle and finish angle between leg and ground\nusually varies between 30 to 60 degree')
plt.annotate(s=f'({start_x}, {round(start_y)})', xy=(start_x, start_y - 50), fontsize=12)
plt.annotate(s=f'({end_x}, {round(end_y)})', xy=(end_x, end_y), fontsize=12)
plt.plot(x, y, label=f'F\u2090 = \u00b5 m g / cos(\u03b8)')
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
