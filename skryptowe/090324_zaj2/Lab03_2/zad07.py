# 7. Tabliczka mnożenia z wykorzystaniem instrukcji while i ewentualnie if (liczymy do 100) - efekt jak w zdaniu zad06.py
i = 1
j = 1
while i < 11:
    j = 1
    while j < 11:
        print('{:>4}'.format(i*j), end="")
        j += 1
    i += 1
    print()