
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy


P = np.array([0.7, 0.2, 0.1])
Q = np.array([0.6, 0.3, 0.1])


H_P = entropy(P, base=2)

cross_entropy = -np.sum(P * np.log2(Q))


kl_divergence = entropy(P, Q, base=2)

print("Entropy:", round(H_P, 4), "bits")
print("Cross-Entropy:", round(cross_entropy, 4), "bits")
print("KL Divergence:", round(kl_divergence, 4), "bits")


labels = ["Class 1", "Class 2", "Class 3"]
x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(8, 4))
plt.bar(x - width / 2, P, width, label="Actual P")
plt.bar(x + width / 2, Q, width, label="Predicted Q")

plt.title("Actual vs Predicted Probability")
plt.xlabel("Classes")
plt.ylabel("Probability")
plt.xticks(x, labels)
plt.legend()
plt.grid(axis="y")
plt.show()


measures = ["Entropy", "Cross-Entropy", "KL Divergence"]
values = [H_P, cross_entropy, kl_divergence]

plt.figure(figsize=(8, 4))
plt.bar(measures, values)
plt.title("Information Measures")
plt.ylabel("Value (bits)")
plt.grid(axis="y")
plt.show()
