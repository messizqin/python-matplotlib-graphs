"""
Generally, the equivalent point indicates the solution is neutralised, which would occur first, because human is hard to
    preciously control the volume just right.
However, according to the table above, it is found that, phenolphthalein changes colour within a pH high than 7 instead
    of equal to 7.
The phenolphthalein reacts with NaOH to change to pink. As the colour changes from pink to transparent, the colour
    would change before pH of seven. The whole line is decreasing, since it meets the end point first, then the
    equivalent point. (First change the colour, then neutralise)
"""

import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import SubplotZero
import numpy as np

"""
a bug found! in SubplotZero, by saying xlabel and ylabel, xzeros and yzeros set the all axis label as xlabel
"""

fig = plt.figure()
ax = SubplotZero(fig, 111)
ax.set_title("Add HCl to NaOH Solution\npH of NaOH Solution")
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

for direction in ["top", "bottom", "left", "right"]:
    ax.axis[direction].set_visible(False)


y = np.linspace(0, 20)
x = -(((y-8)**5)/1000) + 10
plt.plot(x, y)
plt.xlim(0, 25)
plt.ylim(0, 15)
plt.gca().set_aspect('equal')
plt.axhline(7, color="r")
plt.scatter(10, 7, marker="o", color="b")
plt.annotate(s="Equivalence Point (NaOH Solution Neutralised)", xy=(10.5, 7.5))
plt.annotate("Amount of HCl Adding", (9, .4))
plt.annotate("NaOH\nSolution\npH", (1, 12))

plt.fill_between((0, 25), 8.2, 10, color="g", alpha=0.2, label="End Point \n(Phenolphthalein Changes Colour)")

plt.legend()
plt.show()
