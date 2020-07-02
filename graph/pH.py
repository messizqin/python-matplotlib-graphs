"""
pH.py
sketch acid and base pH formula
# from mpl.toolkits.axisartist import Subplotzero
# ax.axis[direction].set_axisline_style("-|>")
# ax.axis[direction].set_visible(True||False)

"""

from matplotlib import pyplot as plt
from mpl_toolkits.axisartist import SubplotZero
import numpy as np

fig = plt.figure()
ax = SubplotZero(fig, 111)
ax.set_title("pH Formula")
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

for direction in ["top", "bottom", "left", "right"]:
    ax.axis[direction].set_visible(False)

# log a(n) n > 0
x = np.linspace(0.01, 20, 2000)
y = np.log10(x)

plt.plot(x, -y, color="m", label="acid pH = -log{}{}[H{}O{}]".format("\N{SUBSCRIPT ONE}",
                                                                     "\N{SUBSCRIPT ZERO}",
                                                                     "\N{SUBSCRIPT THREE}",
                                                                     "\u207A"))
plt.plot(x, 14 + y, color="c", label="base pH = 14 + log{}{}[OH{}]".format("\N{SUBSCRIPT ONE}",
                                                                           "\N{SUBSCRIPT ZERO}",
                                                                           "\u207B"))
plt.scatter(0.1, 1, marker="^", edgecolors="r")
plt.scatter(0.1, 13, marker="v", edgecolors="b")
plt.annotate("HNO{}".format("\N{SUBSCRIPT THREE}"), xy=(1, 1))
plt.annotate("Ba(OH){}".format("\N{SUBSCRIPT TWO}"), xy=(1, 13))

plt.fill_between(x, -y, 14 + y, color="k", interpolate=True, alpha=0.25)

plt.legend(loc="center right")
plt.show()
