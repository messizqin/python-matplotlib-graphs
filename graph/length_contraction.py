from matplotlib import pyplot as plt
import numpy as np

sub_0 = '\N{SUBSCRIPT ZERO}'
sup_2 = '\N{SUPERSCRIPT TWO}'
c = 299792458


def length_contraction(v):
	L0 = 1
	return L0 * ((1-((v**2)/(c**2))) ** 0.5)


x = np.linspace(0, c, 1000)
y = length_contraction(x)

plt.title('Length Contraction')
plt.style.use("fivethirtyeight")
plt.annotate(s=f'L = L{sub_0} sqrt(1 - v{sup_2}/c{sup_2})', xy=[c/2.0, 1/2.0], fontsize=16)
plt.xlabel('length contraction (m)', fontsize=16)
plt.ylabel('static length (m)', fontsize=16)

plt.plot(x, y)
plt.grid()
plt.show()




