# Wykresy pudełkowe (boxplot)
# Utwórz trzy boxploty, reprezentujące rozkłady trzech różnych zestawów danych losowych o 10 próbek. Dodaj etykiety osi, tytuł i legendę.

import matplotlib.pyplot as plt
import numpy as np

#np.random.seed(42)
data1 = 10 * np.random.rand(10)
data2 = 10 * np.random.rand(10)
data3 = 10 * np.random.rand(10)

plt.boxplot([data1, data2, data3], labels=['Zestaw 1', 'Zestaw 2', 'Zestaw 3'])
plt.xlabel('Zestawy danych')
plt.ylabel('Wartości')
plt.title('Boxploty trzech zestawów danych')
plt.grid()
plt.show()
