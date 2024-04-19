# Utwórz dwa osobne wykresy dla funkcji y = sin(x) i y = cos(x)
# (najpierw wyświetlana jest pierwsza funkcja a po jej zamknięciu druga)
# dla x zawierającego 4*pi (2 okresy)
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

x = np.linspace(-10, 10, 100)
y = np.cos(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()