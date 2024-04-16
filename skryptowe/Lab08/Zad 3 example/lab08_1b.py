# 8.1b.
# Otwieramy plik dane.dat i tworzymy nową tablicę result.
# W tablicy tej przechowujemy w postaci listy lub tupli, każdą z wartości bez linijek komentarza
# Dla pliku dane.dat sprawdź za pomocą debugera co robi, każda z linijek kodu

results = []
with open("dane.dat","r") as f:
    #iteracja po wierszach - w każdym kroku wczytywany tylko jeden wiersz
    for line in f:   #  f.readlines()
        #ignorujemy komentarz
        if line[0] == "#": continue
        #wydobycie danych tym razem bardziej "pythonowo"
        all = [float(val) for val in line.split()]
        results.append(all)

#sprawdzamy wynik
for i in results:
    print(i)