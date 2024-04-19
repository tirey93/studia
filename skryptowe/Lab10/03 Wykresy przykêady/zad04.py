# Stwórz wykres słupkowy przedstawiający ilość sprzedanych produktów
# w trzech kategoriach w ciągu ostatnich 5 dni. Dodaj etykiety osi i tytuł.

import matplotlib.pyplot as plt
import numpy as np

days = ['Dzień 1', 'Dzień 2', 'Dzień 3', 'Dzień 4', 'Dzień 5']
category1 = [20, 15, 25, 30, 18]
category2 = [10, 12, 18, 15, 20]
category3 = [25, 30, 22, 20, 15]

plt.bar(days, category1, label='Kategoria 1', color='r')
plt.bar(days, category2, label='Kategoria 2', color='g', bottom=np.array(category1))
plt.bar(days, category3, label='Kategoria 3', color='b', bottom=np.array(category1) + np.array(category2))

plt.xlabel('Dni')
plt.ylabel('Ilość sprzedanych produktów')
plt.title('Wykres słupkowy')
plt.legend()
plt.show()
