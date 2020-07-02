import pandas as pd
from matplotlib import pyplot as plt

_path = input("Please input the data.txt path here: ")
path = _path.replace("\\", "\\\\")

data = pd.read_csv(path, sep="\t")
ages = data["Age"]
all_devs = data["All_Devs"]
python = data["Python"]
javascript = data["JavaScript"]

plt.figure("Salaries")
plt.subplot(2, 1, 1)
plt.title("All Developers")
plt.plot(ages, all_devs, "s--k")

plt.subplot(2, 2, 3)
plt.title("Python")
plt.plot(ages, python, "x:b")

plt.subplot(2, 2, 4)
plt.title("JavaScript")
plt.plot(ages, javascript, "yo-")

plt.tight_layout()
plt.show()


plt.figure("Comparison")
plt.subplot(2, 2, 1)
plt.title("Python Below All Developers", fontdict={
    "family": "serif", "color": "blue", "weight": "normal", "size": 16
})
plt.plot(ages, all_devs, color="k")
plt.plot(ages, python, color="b")
plt.fill_between(ages, all_devs, python, where=python < all_devs, interpolate=True, color="b", alpha=0.25)

plt.subplot(2, 2, 2)
plt.title("Python Above All Developers", fontdict={
    "family": "serif", "color": "blue", "weight": "normal", "size": 16
})
plt.plot(ages, all_devs, color="k")
plt.plot(ages, python, color="b")
plt.fill_between(ages, all_devs, python, where=python > all_devs, interpolate=True, color="r", alpha=0.25)

plt.subplot(2, 2, 3)
plt.title("JavaScript Below All Developers", fontdict={
    "family": "serif", "color": "#FFA500", "weight": "normal", "size": 16
    # orange hex value "#FFA500"
})
plt.plot(ages, all_devs, color="k")
plt.plot(ages, javascript, color="#FFA500")
plt.fill_between(ages, all_devs, javascript, where=javascript < all_devs, interpolate=True, color="c", alpha=0.25)

plt.subplot(2, 2, 4)
plt.title("JavaScript Above All Developers", fontdict={
    "family": "serif", "color": "#FFA500", "weight": "normal", "size": 16
})
plt.plot(ages, all_devs, color="k")
plt.plot(ages, javascript, color="#FFA500")
plt.fill_between(ages, all_devs, javascript, where=javascript > all_devs, interpolate=True, color="m", alpha=0.25)

plt.tight_layout()
plt.show()