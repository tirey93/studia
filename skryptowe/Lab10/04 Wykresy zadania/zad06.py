# Utwórz funkcję f(x) = 1/(x+1) z wybranego zakresu,
# który przynajmniej obejmuję zakres x (-5,5) oraz y (-10,10). Uwaga na wartość x = -1.
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 10, 100)
y = 1/(x+1)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
