import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

plt.title('Simple Harmonic Motion')

epi_path = input('please input the Data or EPI.xlsx file path here: ')
xl_file = pd.ExcelFile(epi_path)

dfs = {sheet_name: xl_file.parse(sheet_name)
          for sheet_name in xl_file.sheet_names}

s1 = dfs['Sheet1']


def to1period(period):
    return float(period/10)


def find_t(m, k=31.387962497709545):
    return float(np.pi*2*np.sqrt(float(m/k)))


def shift_left(arg):
    return arg - 0.05


def shift_right(arg):
    return arg + 0.05


mass = s1['Mass (kg)']
trial1 = list(map(to1period,  s1['Trial 1 (10)']))
trial2 = list(map(to1period,  s1['Trial 2 (10)']))
trial3 = list(map(to1period,  s1['Trial 3 (10)']))
avg = s1['Period Avg']

mass_left = list(map(shift_left, mass))
mass_right = list(map(shift_right, mass))

equation = list(map(find_t, mass))

plt.subplot(2, 1, 1).set_title('Simple Harmonic Motion')
l1 = plt.bar(mass_left, trial1, linewidth=0.1, label='first', width=0.05, color='lightgreen')
l2 = plt.bar(mass, trial2, linewidth=0.1, label='second', width=0.05, color='lightblue')
l3 = plt.bar(mass_right, trial3, linewidth=0.1, label='third', width=0.05, color='gold')
plt.xlabel('mass (kg)')
plt.ylabel('oscillate period (s)')
l4 = plt.plot(mass, avg, label='average', color='magenta')
l5 = plt.plot(mass, equation, color='black', linestyle='--', label='T=2\u03c0 sqrt(m/k)')
for i, x in enumerate(mass_left):
    y = avg[i]
    plt.annotate(y, [x, y])
plt.legend()


def find_k(m, t):
    return float(m/((t/(2*np.pi))**2))


plt.subplot(2, 1, 2).set_title('Calculated Spring Constant')
t1k = list(map(find_k, mass, trial1))
t2k = list(map(find_k, mass, trial2))
t3k = list(map(find_k, mass, trial3))
tak = list(map(find_k, mass, avg))
const = np.average(tak)
# 31.387962497709545
plt.annotate(31.39, [1.6, 31.39])

plt.bar(mass_left, t1k, linewidth=0.1, label='first', width=0.05, color='lightgreen')
plt.bar(mass, t2k, linewidth=0.1, label='second', width=0.05, color='lightblue')
plt.bar(mass_right, t3k, linewidth=0.1, label='third', width=0.05, color='gold')
plt.xlabel('mass (kg)')
plt.ylabel('spring constant (N/m)')
plt.plot(mass, tak, label='average', color='magenta')
plt.axhline(y=const, color='black', linestyle='--', label='k=m/(T/2\u03c0)^2')
for i, x in enumerate(mass_left):
    y = tak[i]
    plt.annotate(round(y, 2), [x, y+1])
plt.legend()

plt.tight_layout()
plt.show()

