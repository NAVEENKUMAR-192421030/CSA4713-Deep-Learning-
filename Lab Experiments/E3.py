import numpy as np
import matplotlib.pyplot as plt

A = np.array([10, 20, 30, 40])
B = np.array([2, 4, 5, 8])

print("Vector A:", A)
print("Vector B:", B)

print("Addition:", A + B)
print("Subtraction:", A - B)
print("Multiplication:", A * B)
print("Division:", A / B)

plt.plot(A + B, marker='o', label='Addition')
plt.plot(A - B, marker='o', label='Subtraction')
plt.plot(A * B, marker='o', label='Multiplication')
plt.plot(A / B, marker='o', label='Division')

plt.title("Vector Arithmetic Operations")
plt.xlabel("Index")
plt.ylabel("Result")
plt.legend()
plt.grid()
plt.show()
