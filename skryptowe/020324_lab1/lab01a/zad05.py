# app05
# wyświetl tabliczkę mnożenia (instrukcja for - 9 kolumn i 9 wierszy)

for i in range(1,11):
    for j in range(1,11):
        print('{:>4}'.format(i*j), end="")
    print()