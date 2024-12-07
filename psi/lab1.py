import random
import perceptron
import numpy as np

print()
print()

eta = 0.01 #wspolczynnik uczenia
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
w = np.random.uniform(low=0.0, high=0.5, size=( 2))

# print(perceptron.output(4, 3, 5, 4 , 0))
# print(perceptron.output_matrix(w, x, 0))

print("-----------------")


print(f"x={x}")
print(f"t={t}")
print(f"w={w}")

# print(perceptron.method())