import random
import perceptron
import numpy as np
import plot

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

print()
print()

eta = 0.01 #wspolczynnik uczenia w drugim zadaniu
x = np.array([
    [-8, 20],
    [-9, 10],
    [-6, 5],
    [2, 20],
    [4, 25],

    [-6, -25],
    [-2, -10],
    [5, 9],
    [1, -10],
    [4, -16],
])
t = np.array([
    1, 1, 1, 1, 1,  0, 0, 0, 0, 0
])
w = np.random.uniform(low=0.0, high=0.5, size=(2))
b = random.uniform(0.0, 0.5)

print("----WEKTORY WEJSCIOWE-------------")
print(f"x={x}")
print(f"t={t}")
print(f"w={w}")
print(f"b={b}")

print("-----------------------")


learning = True
points_learnt = False
epochs = 1

while(learning):
    i = 0
    if points_learnt:
        learning = False

    points_learnt = True
    for xi in x:
        yi = perceptron.output(w, xi, b)
        ei = t[i] - yi

        if ei != 0:
            w = w + ei * np.array([xi[0], xi[1]])
            b = b + ei
            points_learnt = False
    print(f"epochs: {epochs}")
    epochs = epochs + 1
            
print("-----------RESULTS------------")
print(f"w: {w}, b: {b}")


x1 = -b/w[0]
x2 = -b/w[1]

upper, lower = split_list(x)
plot.drawPoints(upper, "red")
plot.drawPoints(lower, "blue")
plot.drawLine(5, 8, [min(x[:,0]), max(x[:,0])])
plot.show()



















