import csv
from matplotlib import pyplot as plt
from collections import Counter
import random


def random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


path = input("please input the data.csv file path here: ")
with open(path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    language_counter = Counter()
    for i in csv_reader:
        language_counter.update(i["LanguagesWorkedWith"].split(";"))

languages = []
popularity = []
for i in language_counter.most_common(15):
    languages.append(i[0])
    popularity.append(i[1])

color = [random_color() for x in languages]


def auto_label(vertical_):
    for index, rectangle in enumerate(vertical_):
        height = rectangle.get_height()
        x_value = rectangle.get_x()
        width = rectangle.get_width()
        plt.text(x_value + width / 2., height, '%d' % height, color=color[index],
                 ha="center", va="bottom")


vertical = plt.bar(languages, popularity, edgecolor="k", color=color)
auto_label(vertical)

plt.title("Top 15 Popular Programming Languages")
plt.grid()

plt.gcf().autofmt_xdate()

plt.show()
