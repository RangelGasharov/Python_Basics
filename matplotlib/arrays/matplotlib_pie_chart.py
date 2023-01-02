import matplotlib.pyplot as plt
import numpy as np

market_share = [77, 18, 2, 3]
software = ['Windows', 'macOS', 'Linux', 'others']
colors = ['blue', 'red', 'green', 'grey']

plt.pie(market_share, labels=software, colors=colors, startangle=180)
plt.title('Example of Pie Plot')
plt.show()
