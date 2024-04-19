# 4. Wykorzystć moduł pickle do zapisania w pliku dane.dat
# wygenerowanych 10000 liczb całkowitych o wartości od 0 do 100.
# Następnie czytamy dane z tego pliku i szukamy, które z wygenerowanych liczb jest najwięcej.

import pickle 
import random
import numpy as np

arr = [random.randrange(101) for x in range(10000)]

with open('dane.dat', 'wb') as f:
    pickle.dump(arr, f)

with open('dane.dat', 'rb') as f:
    res = pickle.load(f) 
    print(res)
    g, count = np.unique(res, return_counts=1)
    print(count[np.argmax(count)])
