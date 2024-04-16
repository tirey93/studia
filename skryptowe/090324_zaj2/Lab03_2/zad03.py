# 3. Dokładamy dodatkowy parametr do funkcji podający jakie liczby chcemy wybrać 
#    suma(typ,a,b), gdzie typ jest typ to True lub False. 
#    True oznacza liczby parzyste, False liczby nieparzyste.
#    Importujemy funkcje z pliku zad02.py i wykorzystujemy je w nowej funkcji suma(typ,a,b).
import zad02
def suma(typ,a,b):
    if typ == True:
        return zad02.sum_even(a,b)
    if typ == False:
        return zad02.sum_odd(a,b)

print(suma(False, 2,7))
print(suma(True, 2,7))