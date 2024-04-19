# 5. Wykorzystanie modułu shelve do zapisania rzutów dwoma kostkami,
# aż do wyrzucenia wartości 12 (zapisujemy kolejne sumy).
# Powtarzamy tą operację jeszcze 10 razy i każdą z serii zapisujemy do nowego zestawu danych.
# Następnie czytamy dane z pliku i podajemy ile rzutów potrzebujemy, w każdej serii
# do wyrzucenia sumy równej 12. Następnie liczymy jedną wartość średnią z wszystkich serii.

import shelve
import random

def licz_rzuty():
    suma = 0
    licz = 1
    while suma != 12:
        kostka1 = random.randrange(6) + 1
        kostka2 = random.randrange(6) + 1

        suma = kostka1 + kostka2
        licz += 1

    return licz
for i in range(10):
    with shelve.open("shelf/db") as f:
        if 'proby' not in f.keys():
            f['proby'] = []
        proby = f['proby']
        proba = licz_rzuty()
        proby.append(proba)
        f['proby'] = proby
        print( f"baza: {f['proby']}")
with shelve.open("shelf/db") as f:
    print( f"baza: {f['proby']}")
    suma =0
    for liczba in f['proby']:
        suma+=liczba
        print(liczba)
    srednia = suma/len(f['proby'])
    print(srednia)



