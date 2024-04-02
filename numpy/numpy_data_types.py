import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int32)
b = np.array([[1, 2, 3], [4, "5", 6], [7, 8, 9]], dtype=np.float32)
example_object = {"2": "Value 2"}
c = np.array([[1, example_object, 3], [4, 5, 6], ["text", 8, 9]])
d = np.array([[1, example_object, 3], [4, 5, 6], ["text", 8, 9]], dtype="<U7")

print(a)
print(f"Type of a: {a.dtype}, type of a[0][0]: {a[0][0].dtype}")
print(b)
print(f"Type of b: {b.dtype}, type of b[1][1]: {b[1][1].dtype}")
print(c)
print(f"Type of example_object: {type(example_object)}")
print(f"Type of c: {c.dtype}, type of c[0][0]: {type(c[0][0])}, type of c[0][1]: {type(c[0][1])}")
print(d)
print(f"Type of d: {d.dtype}, type of d[0][0]: {type(d[0][0])}, type of d[0][1]: {type(d[0][1])}")
