import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

path = input("please input the age.csv file path here: ")
data = pd.read_csv(path)
ids = data["Responder_id"]
ages = data["Age"]

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor="black", log=True)

median_age = 29
red = "#fc4f30"

plt.axvline(median_age, color=red, linewidth=5, label="Age Median")

plt.legend()
plt.title("Ages of Respondents")
plt.xlabel("Ages")
plt.ylabel("Total Respondents")

plt.tight_layout()
plt.show()
