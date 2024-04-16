# 8. Rozwiązywanie równania kwadratowego w dziedzinie liczb rzeczywistych
#    - rozwiązanie tworzymy na początku bez funkcji (kod bez definiowania funkcji) 
#
#    - Następnie docelowo definiujemy funkcje quadratic_equation(a,b,c) zwracjące listę 
#    w postaci [x1, x2, 'komentarz ile jest rozwiązań']
#    Podać przykład uruchomienia funkcji, gdzie mamy jedno rozwiązanie, 2 rozwiązania lub brak rozwiązania.
import math


def quadratic_equation(a,b,c):
    delta = pow(b,2) - 4*a*c
    if int(delta) > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return [x1, x2, "Dwa rozwiązania"]
    elif int(delta) == 0:
        x0 = - b / (2*a)
        return [x0, None, "Jedno rozwiązanie"]
    else:
        return [None, None, "Brak rozwiązań"]

print(quadratic_equation(1,0,0))
print(quadratic_equation(1,0,2))
print(quadratic_equation(1,6,8))
