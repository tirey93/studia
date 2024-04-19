# Utwórz wykres wielolinijkowy przedstawiający zmiany temperatury w ciągu tygodnia dla trzech miast.
# Każde miasto powinno być reprezentowane jako osobna linia.

import matplotlib.pyplot as plt
import numpy as np

days = ['Pon', 'Wt', 'Śr', 'Czw', 'Pt', 'Sob', 'Niedz']
city1_temp = [25, 22, 28, 26, 30, 32, 27]
city2_temp = [20, 18, 25, 22, 28, 30, 26]
city3_temp = [30, 28, 35, 32, 38, 40, 36]

plt.plot(days, city1_temp, label='Miasto 1', marker='o')
plt.plot(days, city2_temp, label='Miasto 2', marker='s')
plt.plot(days, city3_temp, label='Miasto 3', marker='^')

plt.xlabel('Dni tygodnia')
plt.ylabel('Temperatura (°C)')
plt.title('Wykres wielolinijkowy')
plt.legend()
plt.show()
