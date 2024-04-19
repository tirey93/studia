# Na podstawie pliku dane.dat (z poprzednich zajęć) narysować wykres
# przedstwiający drogę w funkcji (czasu) s = f(t),
# gdzie s jest drogą przejechaną od początku jazdy
# i czas, także jest czasem od początku rozpoczęcia ruchu.

import pickle
import matplotlib.pyplot as plt
import numpy as np

with open('../../Lab09/dane.dat', 'rb') as f:
    res = pickle.load(f) 

    time = np.arange(len(res))
    distance = np.cumsum(res)

    plt.plot(time, distance)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
