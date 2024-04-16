# app02
# Do zadania numer 1 dodajemy wyświetlanie typu zmiennej a,b,c (funkcja type())
# Sprawdź jak działa funkcja isinstance() do sprawdzenia i wyświetlenia typu danych danej zmiennej.
a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
c = a + b
print(c)

print(type(c))
print(isinstance(c, int))
print(isinstance(c, float))