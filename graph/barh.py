import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import random


def random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


path = input("please input the data.csv file path here: ")
data = pd.read_csv(path)
language_responses = data["LanguagesWorkedWith"]
language_counter = Counter()
for response in language_responses:
    language_counter.update(response.split(";"))

languages = []
popularity = []
for i in language_counter.most_common(15):
    languages.append(i[0])
    popularity.append(i[1])

color = [random_color() for i in languages]

horizontal = plt.barh(languages, popularity, edgecolor="k", color=color)


def auto_label(horizontal_):
    for index, rectangle in enumerate(horizontal_):
        height = rectangle.get_height()
        width = rectangle.get_width()
        y_value = rectangle.get_y()
        plt.text(width + height/2., y_value, "%d" % width, color=color[index])


auto_label(horizontal)

plt.title("Top 15 Popular Programming Languages")
plt.grid()

plt.tight_layout()
plt.show()
