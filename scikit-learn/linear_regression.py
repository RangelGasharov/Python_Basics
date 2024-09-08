import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

START = 0
END = 100


def logarithmic_growth(time):
    boundary = 150
    start = 5
    growth_constant = 0.0005
    return start * boundary / (start + (boundary - start) * np.e ** (-boundary * growth_constant * time))


t = np.arange(START, END)
linear_function = np.poly1d(np.polyfit(t, logarithmic_growth(t), 1))
print("Score of the approximation by linear function:", r2_score(logarithmic_growth(t), linear_function(t)))
quadratic_function = np.poly1d(np.polyfit(t, logarithmic_growth(t), 2))
print("Score of the approximation by quadratic function:", r2_score(logarithmic_growth(t), quadratic_function(t)))
cubic_function = np.poly1d(np.polyfit(t, logarithmic_growth(t), 3))
print("Score of the approximation by cubic function:", r2_score(logarithmic_growth(t), cubic_function(t)))
quartic_function = np.poly1d(np.polyfit(t, logarithmic_growth(t), 4))
print("Score of the approximation by quartic function:", r2_score(logarithmic_growth(t), quartic_function(t)))

plt.scatter(t, logarithmic_growth(t), c="#d43e1e", s=2)
plt.plot(t, linear_function(t), c="#4aeb12")
plt.plot(t, quadratic_function(t), c="#ebac12")
plt.plot(t, cubic_function(t), c="#1295eb")
plt.plot(t, quartic_function(t), c="#9112eb")
plt.show()
