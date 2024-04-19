# Utwórz wykres liniowy przedstawiający funkcję y=2x+5 dla zakresu
# x od -10 do 10. Dodaj siatkę, etykiety osi i tytuł wykresu.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = 2 * x + 5

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('Wykres liniowy: y = 2x + 5')
plt.show()
