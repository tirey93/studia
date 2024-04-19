# Wygeneruj pary liczb całkowitych x i y losowo z zakresu x (0,100) y (0,100)
# i przedstaw w postaci punktów rozkład tych punktów na płaszczyźnie x,y.
# Losowo wybierz, także różne markery punktów.

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.randint(0, 100, size=(100))
y = np.random.randint(0, 100, size=(100))
colors = np.random.rand(100, 3)

plt.scatter(x, y, c=colors)
plt.grid()
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.title('Wykres punktowy')
plt.legend()
plt.show()
