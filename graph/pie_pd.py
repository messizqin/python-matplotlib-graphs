import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

plt.xkcd()

_path = input("Please input the data.csv file path here: ")
path = _path.replace("\\\\", "\\")

data = pd.read_csv(path)
language_responses = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in language_responses:
    language_counter.update(response.split(";"))

languages = []
popularity = []

print("There are %d languages in total" % len(language_counter))
while True:
    try:
        aim = int(input("How many least popular languages would you like to be shown on the pie chart?"))
        for ind, item in enumerate(language_counter.most_common(len(language_counter))):
            if len(language_counter) - ind <= aim:
                languages.append(item[0])
                popularity.append(item[1])
        break
    except ValueError:
        print("[ValueError] Please input a number bigger than 0 and less than %d" % len(language_counter))
        print("")

# plt.pie(explode=), explode can only be a list, therefore create an interaction to collect explode list.
# e.g. [0, 0, 0.1, 0, 0]
while True:
    print("[Languages]: {}".format(languages))
    want = input("Which one to slightly explode?")
    if want in languages:
        break
    else:
        print("[Value Not Found] Please check and input again")
        print("")

explode = []
for i in languages:
    if i == want:
        explode.append(0.1)
    else:
        explode.append(0)

plt.tight_layout()
plt.title("%d Least Popular Programming Languages 2018" % len(languages), fontdict={
    "family": "serif", "color": "darkred", "weight": "normal", "size": 16})
plt.pie(popularity, explode=explode, labels=languages, autopct="%1.1f%%", shadow=True, startangle=90,
        wedgeprops={"edgecolor": "k"})
plt.show()