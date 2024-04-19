# Utwórz wykres punktowy przedstawiający losowo wygenerowane 50 punktów na płaszczyźnie.
# Użyj różnych kolorów dla punktów. Dodaj siatkę.

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50, 3)

plt.scatter(x, y, c=colors, marker='o')
plt.grid()
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.title('Wykres punktowy')
plt.legend()
plt.show()
