# Utwórz funkcję y = cos(2*pi*x) oraz y = cos(2*pi*x) * exp(x) na jednym wykresie
# dla x z zakresu <0, 2*pi>

import matplotlib.pyplot as plt
import numpy as np
from math import pi

x = np.linspace(0, 2*pi, 100)
y1 = np.cos(2*pi*x)
y2 = np.cos(2*pi*x) * np.exp(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('Wykres liniowy: y = 2x + 5')
plt.show()
