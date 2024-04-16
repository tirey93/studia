# 2. Oblicz sumę liczb parzystych tworząc funkcję sum_even(a,b) z przedziału podanego jako parametry funkcji 
#   (korzystamy z funkcji is_even(a) z zadania zad01.py, która zwraca True lub False 
#   - wykorzystujemy instrukcję from zad01 import * albo import zad01).
#   następnie definiujemy funkcję sum_odd(a,b) do obliczania sumy liczb nieparzystych.

from zad01 import isEven

def sum_even(a, b):
    res = 0
    for i in range(a, b):
        if isEven(i):
            res += i
    return res
def sum_odd(a, b):
    res = 0
    for i in range(a, b):
        if not isEven(i):
            res += i
    return res

