import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.axisartist import SubplotZero


x_data = []
y_data = []

fig = plt.figure()
ax = SubplotZero(fig, 111)
ax.set_title("Add HCl to NaOH Solution\npH of NaOH Solution")
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

for direction in ["top", "bottom", "left", "right"]:
    ax.axis[direction].set_visible(False)

ax.set_xlim(0, 25)
ax.set_ylim(0, 15)
plt.gca().set_aspect('equal')
plt.axhline(7, color="r")
plt.scatter(10, 7, marker="o", color="b")
plt.annotate(s="Equivalence Point (NaOH Solution Neutralised)", xy=(10.5, 7.5))
plt.annotate("Amount of HCl Adding", (9, .4))
plt.annotate("NaOH\nSolution\npH", (1, 12))

plt.fill_between((0, 25), 8.2, 10, color="g", alpha=0.2, label="End Point \n(Phenolphthalein Changes Colour)")


def animation_frame(i):
    x_data.append(-(((i-7.5)**5)/1000.0) + 10)
    y_data.append(i)
    dot, = ax.plot(x_data, y_data, color="#add3e6")
    return dot,


animation = FuncAnimation(fig, func=animation_frame, frames=np.linspace(0, 14, 200)[::-1], interval=10, repeat=False)
plt.legend()
plt.show()
