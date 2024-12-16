import matplotlib.pyplot as plt
import numpy as np
import random
import plot
import perceptron

print()
print()

eta = 0.01
t = np.array([
    [-3, 20],
    [-1, 10],
    [-3, 5],
    [-2, 20],
    [-4, 25],
    [4, -10],
    [2, -10],
    [-1, 5],
    [0, 0],
    [0, 16],

])
m = t.shape[0]

a = random.uniform(-0.25, 0.25)
b = random.uniform(-0.25, 0.25)


print("----WEJŚCIE-------------")
print(f"t={t}")
print(f"a={a}")
print(f"b={b}")

print("-----------------------")

max_iterations = 1000
delta_threshold=0.01

prev_mse = float('inf')
x = t[:, 0]
y = t[:, 1]
for iteration in range(max_iterations):
    y_predicted = a * x + b

    gradient_a = 1/m * sum(2 * (y_predicted - y) * x)
    gradient_b = 1/m * sum(2 * (y_predicted - y))

    a -= eta * gradient_a
    b -= eta * gradient_b

    print(f"iteration: {iteration}")
    print(f"a: {a}, b: {b}")

    mse = perceptron.mean_squared_error(y, y_predicted)
    delta = abs(mse - prev_mse)

    print(f"mse: {mse}")
    print(f"delta: {delta}")
    if delta < delta_threshold:
        print(f"Converged after {iteration + 1} iterations.")
        break

    prev_mse = mse



plot.drawPoints(t, "blue")
# plot.drawLine(x, a * x + b, [min(x[:,0]), max(x[:,0])])
plt.plot(x, a * x + b)
plot.show()