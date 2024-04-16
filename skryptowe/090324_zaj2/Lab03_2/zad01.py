# 1. Sprawdź czy podana liczba jest parzysta czy nieparzysta 
#    (definiujemy funkcję is_even(a), która zwraca True lub False (typ bool))
#    W pliku zad01.py dodajemy w kodzie w odpowiednim miejscu sprawdzenie 
#    czy    if __name__ == '__main__':     w celu uruchomienia zdefiniowanej wcześniej funkcji. 
#    Proszę także zaimportować bibliotekę math poleceniem : from math import *

from math import *
def isEven(number):
    if number % 2 == 0:
        return True
    return False
if __name__ == '__main__':
    print(f"5 is even:{isEven(5)}")
    print(f"10 is even:{isEven(10)}")
