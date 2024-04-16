# 4. Wykorzystując moduł time i funkcję time obliczyć ile trwa pętla
#    składająca się z 100000 iteracji dla listy i dla typu tuple (np. sumowanie).

import random
import time

lista = [random.randrange(1, 100) for i in range(1000000)]
print(type(lista))
tupla = tuple(lista)
print(type(tupla))

start = time.time()
print(sum(lista))
end = time.time()
print(end - start)

start = time.time()
print(sum(tupla))
end = time.time()
print(end - start)