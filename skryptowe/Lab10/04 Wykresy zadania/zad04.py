# 1. Utwórz na jednym wykresie 4 funkcje
# y = sin(x),
# y = cos(x),
# y = 2*cos(x),
# y = cos(x) przesuniety o 45stopni (cos(x + 45stopni)
# dla x zawierającego 4*pi (2 okresy)

import matplotlib.pyplot as plt
import numpy as np
from math import pi

x = np.linspace(-2*pi, 2*pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = 2 * np.cos(x)
y4 = np.cos(x + 45)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
