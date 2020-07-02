import string
import matplotlib.pyplot as plt


listing = input("Please input a list separated by comma").replace(" ", "").split(",")
alpha = string.printable[10:62]


def get_indices(num):
    the = ""
    for i in range(num):
        if i+1 == num:
            the += alpha[i]
            return the
        the += alpha[i]
        the += " + "


t = []
wle = -1
st = ""
while True:
    wle += 1
    if wle == len(listing):
        st += "{}t.append({})".format("\t"*wle, get_indices(wle))
        break
    st += "{}for {} in listing:{}".format("\t"*wle, alpha[wle], "\n")


exec(st)


con = input("Please input a list consists of instance arguments within all "
            "probabilities in separation of comma").replace(" ", "")
if len(str(con.strip())) == 1:
    args = [str(con.strip())[0]]
else:
    args = con.split(",")

# t = ["HTT", "HHH", "TTT"...]
# arg = ["H"]


def unique(a_list): # if sequence does not matter
    c_list = list()
    for each in a_list:
        the_arg = "".join(sorted(each))
        if the_arg in c_list:
            continue
        else:
            c_list.append(the_arg)
    return c_list


t_unique = unique(t)


def wl_count(word, ws):
    num = 0
    for w in ws:
        for i in word:
            if i == w:
                num += 1
    return num


def counted(_t):
    counting = dict()
    for instance in _t:
        # instance = "HHT"
        number = wl_count(instance, args)
        try:
            counting[number] += 1
        except KeyError:
            counting[number] = 1
    return counting


t_ = counted(t)
t_u = counted(t_unique)


def percentage(one, total):
    return float("%.1f" % (one / total * 100.0))


def to_p(y_list, total):
    new_y = []
    for i in y_list:
        new_y.append(percentage(i, total))
    return new_y


y_s = to_p(t_.values(), len(t))
y_u = to_p(t_u.values(), len(t_unique))


plt.subplot(1, 2, 1)
plt.title("Sequence Matters\n[Sequential Probability Distribution]\n{} Total Instance{}\n{} Instance of Containing {}\nrate = {}"
          .format(len(t), str(listing), str(len(t)-t_[0]), str(con), "%.2f%%" % ((len(t)-t_[0])/len(t)*100)))
plt.bar(t_.keys(), y_s, color="#fc4f30")


plt.subplot(1, 2, 2)
plt.title("Sequence Does Not Matter\n[Unique Probability Distribution]\n{} Total Instance{}\n{} Instance of Containing {}\nrate = {}"
          .format(len(t_unique), str(listing), str(len(t_unique)-t_u[0]), str(con),
                  "%.2f%%" % ((len(t_unique)-t_u[0])/len(t_unique)*100)))
plt.bar(t_u.keys(), y_u, color="#008fd5")

plt.tight_layout()
plt.show()
