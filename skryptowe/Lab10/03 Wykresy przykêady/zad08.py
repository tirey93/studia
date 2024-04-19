# Utwórz wykres 3D przedstawiający funkcję z = sin(sqrt(0.5*(x**2) + 0.5*(y**2)))
# dla zakresu x i y od -5 do 5. Dodaj etykiety osi i tytuł.

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(0.5 * x**2 + 0.5 * y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('Oś X')
ax.set_ylabel('Oś Y')
ax.set_zlabel('Oś Z')
ax.set_title('Wykres 3D funkcji sin(sqrt(x^2 + y^2))')
plt.show()

