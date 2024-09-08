import numpy as np
import matplotlib.pyplot as plt

START = 0
END = 100


def logarithmic_growth(time):
    boundary = 150
    start = 5
    growth_constant = 0.0005
    return start * boundary / (start + (boundary - start) * np.e ** (-boundary * growth_constant * time))


t = np.arange(START, END)
linear_function = np.poly1d(np.polyfit(t, logarithmic_growth(t), 1))
print("Approximation by linear_function:\n", linear_function(t))

plt.scatter(t, logarithmic_growth(t), c="#d43e1e", s=2)
plt.plot(t, linear_function(t))
plt.show()
