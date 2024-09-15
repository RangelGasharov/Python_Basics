import matplotlib.pyplot as plt
from scipy import stats

height_in_meters = [156.3, 158.9, 160.8, 179.6, 156.6, 165.1, 165.9, 156.7, 167.8, 160.8]
ring_diameter_in_millimeters = [47.1, 46.8, 49.3, 53.2, 47.7, 49.0, 50.6, 47.1, 51.7, 47.8]

slope, intercept, r, p, std_err = stats.linregress(height_in_meters, ring_diameter_in_millimeters)


def prediction_ring_diameter(x):
    return slope * x + intercept


prediction = list(map(prediction_ring_diameter, height_in_meters))

print(f"150cm: {prediction_ring_diameter(150)} mm")
print(f"190cm: {prediction_ring_diameter(190)} mm")
print("Relationship R = ", str(r))

plt.scatter(height_in_meters, ring_diameter_in_millimeters)
plt.plot(height_in_meters, prediction)
plt.show()
