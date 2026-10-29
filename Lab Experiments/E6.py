x = 10.0
lr = 0.1
for method in ["GD", "SGD", "Momentum", "Adam"]:
    x, v, m, s = 10.0, 0.0, 0.0, 0.0
    for t in range(1, 101):
        g = 2 * x
        if method == "SGD": g *= 1.1  
        if method == "Momentum": v = 0.9 * v + g; g = v
        if method == "Adam":
            m = 0.9 * m + 0.1 * g
            s = 0.999 * s + 0.001 * g * g
            g = (m / (1 - 0.9**t)) / ((s / (1 - 0.999**t))**0.5 + 1e-8)
        x -= lr * g
    print(method, ":", round(x, 6))
