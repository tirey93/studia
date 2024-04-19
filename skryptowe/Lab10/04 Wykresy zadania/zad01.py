# Utwórz trzy funkcje na jednym wykresie y = x, y = 0.5*x**2, y = sqrt(x**4)
# x = np.arange(-5., 5., 0.1)
# Osie x i y mają być proporcjonalne, wyświetl siatkę.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y1 = x
y2 = 0.5*x**2
y3 = np.sqrt(x**4)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
