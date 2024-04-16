# 9. Z wykładu definiujemy funkcję silnia(a)
#  i porównujemy wyniki z funkcją math.factorial().
#  Śledzimy za pomocą debugera wykonanie rekurencyjne naszej funkcji silnia.
#  Dodatkowo wykorzystujemy funkcję time() z biblioteki time do sprawdzenia,
#  które z obliczeń działa szybciej (sprawdzić dla dość dużych liczb)
import math
import random
import time


def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    return 1

for i in range(100):
    fact = random.randint(800, 1000)
    t1 = time.time()

    silnia(fact)
    t_silnia =  time.time() - t1

    t1 = time.time()
    math.factorial(fact)
    t_math = time.time() - t1

    print(f"{fact}! - czas mojej funkcji: {t_silnia}, czas z math: {t_math}")
