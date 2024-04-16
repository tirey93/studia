#app03
#Wyświetl n kolejnych liczb (instrukcja while)
#Liczbę n podajemy z klawiatury. Pierwsza liczba jest 1.
#Sprawdź na końcu działanie funkcji vars()

n = int(input("Podaj liczbe: "))
i = 1
while i <= n:
    print(i)
    i += 1
print(vars())