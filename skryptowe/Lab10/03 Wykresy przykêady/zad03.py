# Utwórz histogram z 100 losowo wygenerowanymi liczbami z rozkładu normalnego.
# Ustaw odpowiednie etykiety i tytuł.

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = np.random.randn(100)

plt.hist(data, bins=20, color='green', alpha=0.7)
plt.xlabel('Wartości')
plt.ylabel('Częstość')
plt.title('Histogram')
plt.show()