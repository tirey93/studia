# 8.1c.
# Otwieramy plik dane.dat i tworzymy nową tablicę results.
# W tablicy tej przechowujemy w postaci listy lub tupli, każdą z wartości bez linijek komentarza
# Następnie liczymy sumę z pierwszej kolumny liczb
# Dodajemy nowy wiersz do pliku z wartościami zerowymi, taki aby nie generował błędu przy ponownym czytaniu danych


# Otwarcie pliku i generowanie listy
results = []
with open("dane.dat","r") as file:
    results = [[float(val) for val in line.split()]
     for line in file if line[0] != "#"]

# Wyswietl tablicę
for line in results:
    print(line)

# oblicz sumę z pierwszej kolumny liczb
print(sum([x[0] for x in results]))

# dodaj nową linijkę do listy
f = open("dane.dat","a+")
f.write('\n0.000000 0.000000 0.000000')
f.close()