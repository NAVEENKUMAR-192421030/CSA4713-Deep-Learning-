import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

result = v1 + v2

print("Vector 1:", v1)
print("Vector 2:", v2)
print("Vector Addition:", result)

plt.plot(v1, label="Vector 1", marker="o")
plt.plot(v2, label="Vector 2", marker="o")
plt.plot(result, label="Addition", marker="o")

plt.title("Vector Operations")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()
