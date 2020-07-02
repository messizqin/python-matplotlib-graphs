import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

plt.xkcd()

path = input("Please input the data.csv file path here: ")
data = pd.read_csv(path)
language_responses = data["LanguagesWorkedWith"]
language_counter = Counter()
for i in language_responses:
    language_counter.update(i.split(";"))

print("There are %d languages in total. " % len(language_counter))
while True:
    want = input("How many languages to show on the pie chart?")
    try:
        if 0 < int(want) <= len(language_counter):
            break
        else:
            print("[Invalid Input] input a number between 0 and %d" % len(language_counter))
            print("")
    except ValueError:
        print("[ValueError] please input a number between 0 and %d" % len(language_counter))
        print("")

languages = []
popularity = []
for item in language_counter.most_common(int(want)):
    languages.append(item[0])
    popularity.append(item[1])


def get_explode(language):
    lan_p = ""
    for v, q in enumerate(language):
        lan_p += "[{}] {}; ".format(v + 1, q)
    while True:
        print(lan_p)
        try:
            aim = int(input("which one to explode slightly? please input a number to select. "))
            if 0 < aim <= len(language):
                exploding = []
                for k in range(len(language)):
                    if k == aim - 1:
                        exploding.append(0.1)
                    else:
                        exploding.append(0)
                return exploding
            else:
                print("[ValueError] please input a number in range of 0 to {}".format(len(language)))
                print("")
        except ValueError:
            print("[ValueError] please input a number to select")


plt.pie(popularity, labels=languages, explode=get_explode(languages),
        wedgeprops={"edgecolor": "k"}, startangle=90, autopct="%1.1f%%")
plt.title("Top %d Popular Programming Languages 2018" % len(languages))
plt.tight_layout()
plt.show()
