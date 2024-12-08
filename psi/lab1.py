import random
import perceptron
import numpy as np

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
w = np.random.uniform(low=0.0, high=0.5, size=(x.shape[0], 2))
b = np.random.uniform(low=0.0, high=0.5, size=(x.shape[0]))

print("----WEKTORY WEJSCIOWE-------------")
print(f"x={x}")
print(f"t={t}")
print(f"w={w}")
print(f"b={b}")

print("-----------------------")

i = 0
for xi in x:
    yi = perceptron.output(w, xi, b)
    ei = t[i] - yi

    if ei == 0:
        print("ei == 0")
        pass
    else:
        w = w + ei * np.array([xi[0], xi[1]])
        b = b + ei
        print(f"e1= {ei}")
        print(f"w= {w}")
        print(f"b= {b}")

    print()
        


    i = i + 1

















