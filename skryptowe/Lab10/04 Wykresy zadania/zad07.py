# Utwórz w jednym oknie w dowolnej konfiguracji
# cztery wykresy funkcji y = sin(x), y=cos(x), y=sin(2*x), y=cos(2*x)
import matplotlib.pyplot as plt
import numpy as np
from math import pi

x = np.linspace(-2*pi, 2*pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2*x)
y4 = np.cos(2*x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
