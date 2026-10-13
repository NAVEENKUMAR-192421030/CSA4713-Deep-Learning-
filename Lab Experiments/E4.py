
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

# Probability Distribution
x = np.linspace(-4, 4, 100)
y = norm.pdf(x, loc=0, scale=1)

plt.figure(figsize=(8, 4))
plt.plot(x, y, label="Normal Distribution")
plt.title("Normal Probability Distribution")
plt.xlabel("X")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()

# Binomial Distribution
k = np.arange(0, 11)
p = binom.pmf(k, 10, 0.5)

plt.figure(figsize=(8, 4))
plt.bar(k, p)
plt.title("Binomial Probability Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.grid(True)
plt.show()

# Bayes' Theorem
p_disease = 0.01
p_positive_given_disease = 0.95
p_positive_given_no_disease = 0.05

p_positive = (
    p_positive_given_disease * p_disease
    + p_positive_given_no_disease * (1 - p_disease)
)

p_disease_given_positive = (
    p_positive_given_disease * p_disease / p_positive
)

print("Probability of Disease:", p_disease)
print("Probability of Positive Test:", round(p_positive, 4))
print("Probability of Disease Given Positive Test:",
      round(p_disease_given_positive, 4))
