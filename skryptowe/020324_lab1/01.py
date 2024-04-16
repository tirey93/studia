# mając zmienne a=2, b=5, z=90
import math

a = 2
b = 5
z = 90
# - pierwiatek kwadratorwy help(math.sqrt) - pierwiastek(a^2+3*b^2) + 15
print((math.sqrt(a) + 3*math.sqrt(b)) + 15)
# - cosinus - cosinus 120 stopni
print(math.cos(math.radians(120)))
# - sinus - sinus 90 stopni - czyli paramterem funkcji bedzie zmienna 'z',
print(math.sin(math.radians(z)))
# - sinus - z wartośi w radianach 2*pi (czy wyjdzie 0?)
# 	(jak nie wyjdzie 0 to zaokrąglamy do wynik do dwóch miejsc po przecinku - 	szukamy funkcję do zaokrąglania w helpie z rozszerzeniem chm)
print(round(math.sin(2*math.pi), 2))
# - zamiana radiany na stopnie - liczba pi ile to stopni (pi pobieramy jako math.pi)
print(math.degrees(math.pi))
# - zamiana stopni na radiany - 180 stopni ile to radianów
print(math.radians(180))













