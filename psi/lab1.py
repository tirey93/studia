import random
import perceptron
import numpy as np
import plot

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

print()
print()

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
    1, 
    1, 1, 1, 1,  0, 0, 0, 0, 
    0
])
w = np.random.uniform(low=-0.25, high=0.25, size=(2))
b = random.uniform(-0.25, 0.25)

print("----WEKTORY WEJSCIOWE-------------")
print(f"x={x}")
print(f"t={t}")
print(f"w={w}")
print(f"b={b}")

print("-----------------------")


points_learnt = False
epochs = 1

while(True):
    if points_learnt:
        break

    points_learnt = True
    # if True:
        # xi = x[0]
    for i, xi in enumerate(x):
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

print(x1)
print(x2)
upper, lower = split_list(x)
plot.drawPoints(upper, "red")
plot.drawPoints(lower, "blue")
plot.drawLine(x1, x2, [min(x[:,0]), max(x[:,0])])
plot.show()



print("---------DETERMINING POINTS---------")
p1 = np.array([-10, -10])
p2 = np.array([-3, 15])
p3 = np.array([15, -25])
p4 = np.array([3, 0])
print(f"{p1}, expected: 1, result: {perceptron.output(w, np.array(p1), b)}")
print(f"{p2}, expected: 1,result: {perceptron.output(w, np.array(p2), b)}")
print(f"{p3}, expected: 0,result: {perceptron.output(w, np.array(p3), b)}")
print(f"{p4}, expected: 0,result: {perceptron.output(w, np.array(p4), b)}")










