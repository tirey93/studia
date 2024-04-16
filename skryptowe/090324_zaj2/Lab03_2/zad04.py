# 4. Na podstawie funkcji z zadania zad03.py, tworzymy funkcję sum_all(a,b), 
#    która liczy sumę liczb parzystych i nieparzystych razem. 
#    Nie definiujemy od sumowania wszystkich liczb od początku tylko wykorzystujemy funkcję sum(typ,a,b)
#  Dodatek:
#    Na końcu zadania proszę wykonać polecenie print('Wynik =',sqrt(9)) bez importu biblioteki math. 
#    Czy polecenie działa i dlaczego mimo braku polecenia import w pliku zad04.py?

import zad03
import math

def sum_all(a,b):
    return zad03.suma(True, a,b) + zad03.suma(False, a,b)

print(sum_all(2,7))
print('Wynik =',math.sqrt(9))