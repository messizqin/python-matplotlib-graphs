"""
according to Engineering Statistics Handbook, the value m is a control which indicate interplay of purity and efficiency,
which signals sample size, how many measurements are affordable to throw away.

support multiple sets of y values

1. Why and When to Optimize Efficiency Time Purity, Benno List, 31/07/2002, https://www.desy.de/~blist/notes/whyeffpur.ps.gz
1. Numpy Builtin Outlier Rejection, Benjamin Bannier, https://stackoverflow.com/questions/11686720/is-there-a-numpy-builtin-to-reject-outliers-from-a-list
2. Engineering Statistics Handbook, Information Technology Laboratory (ITL), https://www.itl.nist.gov/div898/handbook/eda/section3/eda35h.htm
"""

import pandas as pd
import tkinter as tk
import random

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import numpy as np

left_shift = 0
upper_shift = 0
shift_rate = 0.65
left_conner = [0.42, 7.5]
average_color = 'blue'
average_fill = 'cyan'

abs_excel_file = pd.ExcelFile('/Users/qinyiqi/PycharmProjects/Medium/graphics/Data for EPI.xlsx')

dfs = {sheet_name: abs_excel_file.parse(sheet_name) for sheet_name in abs_excel_file.sheet_names}
s1 = dfs['Sheet1']

# col_names<x_col, y_col1, y_col2...>
col_names = ['Mass (kg)', 'Trial 1 (10)', 'Trial 2 (10)', 'Trial 3 (10)']

# x_val<list>
x_val = s1[col_names[0]]
# y_val<list<np.array>>
y_val = []


# linear regression = (x_var:number, *args):y_var
def equation(x_var, k=31.4):
    return 2 * np.pi * np.sqrt(float(x_var) / k)


def data_processor(qs):
    return float(qs)/10


for cn in col_names[1:]:
    y_val.append(np.array(list(map(data_processor, s1[cn]))))

# validation
# print(s1)
# print(x_val)
# print(y_val)
# exit()


def main_plot():
    plt.title('Harmonic Motion')
    plt.xlabel('period(s)')
    plt.ylabel('distance(m)')
    if len(x_use[0]) != 0:
        for i, xs in enumerate(x_use):
            if i == len(x_use) - 1:
                plt.plot(xs, list(y_use[i]), color=average_color, alpha=0.5, label='average')
                const = np.average(list(y_use[i]))
                plt.axhline(y=const, color=average_color, linestyle='-.')
                plt.fill_between(xs, const, list(y_use[i]), color=average_fill, alpha=0.25)
            else:
                plt.plot(xs, list(y_use[i]), color=colors[i], alpha=0.5, label='trial %d' % int(i+1))
    plt.legend(loc='upper left')
    print('standard deviation: ', std_avg)


y_avg = []
for ho in range(len(y_val[0])):
    co = 0
    pl = 0
    for ve in range(len(y_val)):
        co += 1
        pl += y_val[ve][ho]
    y_avg.append(float(pl/co))

y_val.append(y_avg)


def concat1(arr):
    res = []
    for i in arr:
        res.append(i)
    return np.array(res)


def concat2(arr):
    res = []
    for brr in arr:
        res.append(concat1(brr))
    return res


def flat2(arr):
    res = []
    for brr in arr:
        for crr in brr:
            res.append(crr)
    return res


y_use = concat2(y_val)
x_use = concat1(x_val)
std_avg = 0

matplotlib.use('TkAgg')
plt.style.use('ggplot')
root = tk.Tk()

fig = plt.figure(1)
plt.ion()

sigma = 0
colors = ["#%06x" % random.randint(0, 0xFFFFFF) for x in range(len(y_val)-1)]


def generator():
    a = -1
    while True:
        a += 1
        yield a


g = generator()


def gen():
    return int(g.__next__())


def to_abs(num):
    return abs(num)


# [[useful<dict>, outliers<dict>]...]
def reject_outliers(data_frame, m=1):
    global std_avg
    y_should = np.array(list(map(equation, x_val)))
    res = []
    for raw_data in data_frame:
        data = np.array(list(map(to_abs, y_should-raw_data)))
        std_avg = np.std(data)
        mean = np.mean(data)
        res.append([{}, {}])
        for (i, d) in enumerate(data):
            if abs(d - mean) < float(m) * std_avg:
                res[-1][0][i] = raw_data[i]
            else:
                res[-1][1][i] = raw_data[i]
    return res


canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()


def update():
    global x_use, y_use
    x_use = []
    y_use = []
    plt.clf()
    con = reject_outliers(y_val, sigma)
    for i, uo in enumerate(con):
        u_ys = uo[0].values()
        o_ys = uo[1].values()
        u_xs = []
        o_xs = []

        for k in uo[0].keys():
            u_xs.append(x_val[k])

        for j, k in enumerate(uo[1].keys()):
            o_xs.append(x_val[k])
            plt.annotate(
                s='  (%.2f, %.2f)' % (x_val[k], y_val[i][k]),
                xy=[float(x_val[k])-left_shift*(j+1)*shift_rate, float(y_val[i][k])+upper_shift*(j+1)*shift_rate]
            )

        if i == len(con) - 1:
            plt.scatter(u_xs, u_ys, color=average_color, alpha=.4, linewidth=2)
            plt.scatter(o_xs, o_ys, color=average_color, linewidth=4)
        else:
            plt.scatter(u_xs, u_ys, color=colors[i], alpha=.4, linewidth=2)
            plt.scatter(o_xs, o_ys, color=colors[i], linewidth=4)

        x_use.append(u_xs)
        y_use.append(u_ys)
    fig.canvas.draw()
    main_plot()


entry_var = tk.StringVar(root, 'graph')


def save():
    plt.savefig(entry_var.get())


def deviation(m):
    global sigma
    sigma = float(m)
    var.set(sigma)


def re_color():
    global colors
    colors = ["#%06x" % random.randint(0, 0xFFFFFF) for x in range(len(y_val))]
    update()


var = tk.DoubleVar(root, 0)
plot_widget.grid(row=gen(), column=0)
tk.Button(root, text='color', command=re_color).grid(row=gen(), column=0)
tk.Label(root, text='save file name').grid(row=gen(), column=0)
tk.Entry(root, textvariable=entry_var).grid(row=gen(), column=0)
tk.Button(root, text='Save', command=save).grid(row=gen(), column=0)
tk.Button(root, text="Update", command=update).grid(row=gen(), column=0)
scale_widget = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL, resolution=0.01, length=400, command=deviation)
scale_widget.grid(row=gen(), column=0)
entry_widget = tk.Entry(root, textvariable=var)
entry_widget.grid(row=gen(), column=0)


def entry_event(the_val):
    the_val = float(the_val)
    if 0 <= the_val <= 10:
        scale_widget.set(the_val)
        update()


entry_widget.bind("<Return>", lambda event: entry_event(var.get()))
update()

root.mainloop()
