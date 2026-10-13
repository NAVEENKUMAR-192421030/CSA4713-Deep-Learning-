import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = A + B

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Addition:\n", C)

plt.imshow(C, cmap="viridis")
plt.colorbar(label="Value")
plt.title("Matrix Addition Heatmap")
plt.xlabel("Column")
plt.ylabel("Row")

for i in range(C.shape[0]):
    for j in range(C.shape[1]):
        plt.text(j, i, C[i, j], ha="center", va="center", color="white")

plt.show()
