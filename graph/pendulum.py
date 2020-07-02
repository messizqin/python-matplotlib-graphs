from math import pi
import pandas as pd
import matplotlib.pyplot as plt


def get_consent(statement):
    while True:
        aim = input("{}?: (y/n)".format(statement))
        if aim == "y" or aim == "":
            return True
        elif aim == "n":
            return False
        else:
            print("Invalid Input")
            print("")


path = input("please input the physics.csv file path here: ")
data = pd.read_csv(path)
_length = data["Length"]
_time = data["Time"]

length = []
for i in _length:
    length.append(i)

time = []
for i in _time:
    time.append(float(i))

lens = []
len_idx = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
for i in len_idx:
    lens.append(i)
    lens.append(i + 0.03)
    lens.append(i + 0.06)
    if i == 0.2:
        continue
    lens.append(i + 0.09)
    lens.append(i + 0.12)

g = 9.8
T_real = []
T_test = []
for d in lens:
    T_real.append(2*pi*((d/g)**0.5))
for i in time:
    T_test.append(float(i/10))


def original(x):
    from Matplotlib.pyplot import Edit
    y = []
    for p in len_idx:
        y.append(2 * pi * ((p / 9.8) ** 0.5))
    op, rd = Edit.stage(x, y, 0.12, end=True)
    op[1] = 00.26
    for idx, the_x in enumerate(op):
        the_y = rd[idx]
        plt.annotate(s="%.2f" % the_y, xy=(the_x - 0.04, the_y + 0.1))
    plt.plot(op, rd, "o--m", label="What Period Should be")


style_list = ['default', 'classic'] + sorted(style for style in plt.style.available if style != 'classic')

if get_consent("loops the styles"):
    a = 0
    while True:

        plt.title("What Period Should be & Test Results Comparison")
        plt.ylim(0.8, 2.8)
        plt.plot(lens, T_real, color="m", label="What Period Should be")
        plt.scatter(lens, T_real, color="m", marker="o")
        for i, d in enumerate(lens):
            plt.annotate(s="%.2f" % T_real[i], xy=(d, T_real[i] + 0.1))

        plt.plot(lens, T_test, color="c", marker=">", label="Test Results")
        for i, d in enumerate(lens):
            plt.annotate(s="%.2f" % T_test[i], xy=(d, T_test[i] - 0.1))
        plt.xlabel("Period (second)")
        plt.ylabel("Length (meter)")
        plt.legend(loc="upper left")

        print("[{}]".format(style_list[a]))
        print("")
        plt.style.use(style_list[a])
        plt.show()
        if get_consent("continue"):
            pass
        else:
            a += len(style_list)
        a += 1
        if a >= len(style_list):
            print("There are %d available styles in total. " % len(style_list))
            quit()
else:
    original(len_idx)
    plt.title("[Detail] What Period Should be & Test Results Comparison")
    plt.ylim(0.8, 2.8)

    # plt.plot(lens, T_real, color="k", label="Real Period")
    # plt.scatter(lens, T_real, color="k", marker="o")
    # for i, d in enumerate(lens):
    #     plt.annotate(s="%.2f" % T_real[i], xy=(d, T_real[i] + 0.1))

    plt.plot(lens, T_test, color="c", label="Test Results", marker=">")
    for i, d in enumerate(lens):
        plt.annotate(s="%.2f" % T_test[i], xy=(d, T_test[i] - 0.1))
    plt.xlabel("Period (second)")
    plt.ylabel("Length (meter)")
    plt.legend(loc="upper left")
    plt.show()


"""
average
"""


_length = ['20', '40', '60', '80', '100', '120', '140']
_time = ['8.93', '12.73', '15.66', '17.91', '20.11', '21.87', '23.70']

length = []
for i in _length:
    length.append(int(i)*0.01)

time = []
for i in _time:
    time.append(float(i)/10)

T_test = time

g = 9.8
T_real = []
for i in length:
    T_real.append(2*pi*((i/g)**0.5))

plt.title("[Average] What Period Should be & Test Results Comparison")
plt.xlabel("Period (second)")
plt.ylabel("Length (meter)")

plt.plot(length, T_real, color="m", label="What Period Should be", marker="o")
for i, d in enumerate(length):
    plt.annotate("%.2f" % T_real[i], (d, T_real[i] + .1))

plt.plot(length, T_test, color="c", label="Test Results", marker=">")
for i, d in enumerate(length):
    plt.annotate("%.2f" % T_test[i], (d, T_test[i] - .1))
plt.ylim(0.7, 2.6)

plt.legend(loc="center, left")
plt.show()
