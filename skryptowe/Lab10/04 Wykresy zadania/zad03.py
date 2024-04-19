# Utwórz wykres 3D przedstawiający funkcję z = x**2 + y**2 dla zakresu
# x oraz y od -10 do 10. Dodaj siatkę, etykiety osi i tytuł wykresu.

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('Oś X')
ax.set_ylabel('Oś Y')
ax.set_zlabel('Oś Z')
plt.show()
