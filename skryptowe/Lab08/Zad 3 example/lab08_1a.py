# 8.1a.
# Otwieramy plik dane.dat i tworzymy nową tablicę result.
# W tablicy tej przechowujemy w postaci listy lub tupli, każdą z wartości bez linijek komentarza
# Dla pliku dane.dat sprawdź za pomocą debugera co robi, każda z linijek kodu
results = []
# wczytujemy wiersze, pomijamy komentarz
with open("dane.dat", "r") as f:
    lines = f.readlines()[4:]
# wydobywamy dane z wczytanych ciągów znaków
for line in lines:
    # dzielimy wiersz na pola
    fields = line.split()
    # zamieniamy napisy na liczby
    time = float(fields[0])
    pos = float(fields[1])
    vel = float(fields[2])
    # dopisujemy do listy z wynikami
    all = (time, pos, vel)
    results.append(all)
# sprawdzamy wynik
for i in results:
    print(i)
