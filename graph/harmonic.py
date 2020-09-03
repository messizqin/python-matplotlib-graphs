import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

xl_file = pd.ExcelFile('/Users/qinyiqi/PycharmProjects/Medium/graphics/Data for EPI.xlsx')

dfs = {sheet_name: xl_file.parse(sheet_name)
          for sheet_name in xl_file.sheet_names}

s1 = dfs['Sheet1']


def to1period(period):
    return float(period/10)


def find_t(m, k=31.387962497709545):
    return float(np.pi*2*np.sqrt(float(m/k)))


mass = s1['Mass (kg)']
trial1 = list(map(to1period,  s1['Trial 1 (10)']))
trial2 = list(map(to1period,  s1['Trial 2 (10)']))
trial3 = list(map(to1period,  s1['Trial 3 (10)']))
avg = s1['Period Avg']

equation = list(map(find_t, mass))

plt.subplot(1, 2, 1)
l1 = plt.scatter(mass, trial1, linewidth=0.1, label='trial 1')
l2 = plt.scatter(mass, trial2, linewidth=0.1, label='trial 2')
l3 = plt.scatter(mass, trial3, linewidth=0.1, label='trial 3')
plt.xlabel('mass (kg)')
plt.ylabel('oscillate period (s)')
l4 = plt.plot(mass, avg, label='average')
l5 = plt.plot(mass, equation, color='r', linestyle='-.', label='T=2\u03c0 sqrt(m/k)')
plt.grid()
plt.legend()


def find_k(m, t):
    return float(m/((t/(2*np.pi))**2))


plt.subplot(1, 2, 2)
t1k = list(map(find_k, mass, trial1))
t2k = list(map(find_k, mass, trial2))
t3k = list(map(find_k, mass, trial3))
tak = list(map(find_k, mass, avg))
const = np.average(tak)
# 31.387962497709545

plt.scatter(mass, t1k, linewidth=0.1, label='trial 1')
plt.scatter(mass, t2k, linewidth=0.1, label='trial 2')
plt.scatter(mass, t3k, linewidth=0.1, label='trial 3')
plt.xlabel('mass (kg)')
plt.ylabel('spring constant (N/m)')
plt.plot(mass, tak, label='average', color='b')
plt.axhline(y=const, color='r', linestyle='-.', label='k=m/(T/2\u03c0)^2')

plt.fill_between(mass, const, tak, color="cyan", alpha=0.25)

plt.legend()

plt.tight_layout()
plt.show()
