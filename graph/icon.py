# icons [blue, black, red]
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist import SubplotZero
from matplotlib import patches


def icon():
    def sketch(color, above, below, lw):
        fig = plt.figure(1)
        ax = SubplotZero(fig, 111)
        fig.add_subplot(ax)

        for direction in ["top", "bottom", "left", "right"]:
            ax.axis[direction].set_visible(False)

        ac = patches.Arc(xy=(30, 70), width=30, height=20, angle=30, theta1=0, theta2=200, color=color,
                         linewidth=int(lw))
        ax.add_patch(ac)

        x_va = [42, 48, 63, 82]
        y_va = [40, 14, 44, 14]

        plt.plot(x_va, y_va, linewidth=int(lw), color=color)

        x_ha = [70, 80]
        y_ha = [70, 100]
        plt.plot(x_ha, y_ha, linewidth=int(lw), color=color)

        # hash line

        h1_x = [70, 82]
        h1_y = [70, 14]
        plt.plot(h1_x, h1_y, color=color, linewidth=int(lw), linestyle="dotted")

        # unsure hash line
        x_above = above[0]
        y_above = above[1]
        x_below = below[0]
        y_below = below[1]

        x1 = [79, x_above]
        y1 = [100, y_above]
        plt.plot(x1, y1, color=color, linewidth=int(lw), linestyle="dotted")

        x2 = [38, x_below]
        y2 = [44, y_below]
        plt.plot(x2, y2, color=color, linewidth=int(lw), linestyle="dotted")

        plt.xlim(-10, 130)
        plt.ylim(-10, 130)
        plt.show()

    be = [20, 60]
    ab = [43, 78]

    def value(being, va):
        newbie = list()
        newbie.append(being[0] + int(va))
        newbie.append(being[1] - int(va))
        return newbie

    be = value(be, 2)

    for c in ["#008fd5", "#fc4f30", "#e5ae37", "#6d904f", "k"]:
        sketch(c, ab, be, 15)


def cross():
    fig = plt.figure(1)
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)

    for direction in ["top", "bottom", "left", "right"]:
        ax.axis[direction].set_visible(False)

    plt.plot([0, 50], [100, 50], color="#008fd5", linewidth=25)
    plt.plot([100, 50], [100, 50], color="#fc4f30", linewidth=25)
    plt.plot([0, 50], [0, 50], color="#6d904f", linewidth=25)
    plt.plot([100, 50], [0, 50], color="#e5ae37", linewidth=25)
    plt.scatter(50, 50, linewidths=70, color="k", zorder=10)
    plt.scatter(50, 50, linewidths=60, color="k", zorder=10)
    plt.scatter(50, 50, linewidths=50, color="k", zorder=10)
    plt.scatter(50, 50, linewidths=40, color="k", zorder=10)
    plt.scatter(50, 50, linewidths=30, color="k", zorder=10)
    plt.scatter(50, 50, linewidths=20, color="k", zorder=10)
    plt.scatter(50, 50, linewidths=10, color="k", zorder=10)

    plt.xlim(-10, 110)
    plt.ylim(-10, 110)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def cross_delete():
    fig = plt.figure(1)
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)

    for direction in ["top", "bottom", "left", "right"]:
        ax.axis[direction].set_visible(False)
    plt.plot([0, 20], [60, 60], linewidth=25, color="#fc4f30")
    plt.plot([20, 60], [60, 0], linewidth=25, color="#fc4f30", linestyle="dotted")
    plt.plot([60, 80], [0, 0], linewidth=25, color="#fc4f30")

    plt.plot([0, 20], [0, 0], linewidth=25, color="#008fd5")
    plt.plot([20, 60], [0, 60], linewidth=25, linestyle="dotted", color="#008fd5")
    plt.plot([60, 80], [60, 60], linewidth=25, color="#008fd5")
    plt.xlim(-10, 90)
    plt.ylim(-20, 80)
    plt.show()


icon()
cross()
cross_delete()
