import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y = [1, 2, 4, 7, 13, 25, 45, 74, 92, 100]

plt.plot(x, y, color="red", linewidth=0.5)
plt.title("Simple Graph with matplotlib")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.show()
