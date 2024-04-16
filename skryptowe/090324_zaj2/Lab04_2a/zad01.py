# 1. Rozwiązywanie równania kwadratowego w dziedzinie liczb urojonych (zespolonych)
#    definiujemy funkcje quadratic_equation_im(a,b,c) zwracjące listę w postaci [x1, x2]
#    Podać przykład uruchomienia funkcji.
import math


def quadratic_equation_im(a,b,c):
    delta = pow(b,2) - 4*a*c
    if int(delta) > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return [x1, x2]
    elif int(delta) == 0:
        x0 = - b / (2*a)
        return [x0, None]
    elif int(delta) < 0:
        x1 = complex((float(-b) / 2.0 * float(a)), (math.sqrt(abs(delta)) / (2.0 * a)))
        x2 = complex((float(-b) / 2.0 * float(a)), -((math.sqrt(abs(delta))) / (2.0 * a)))
        return [x1, x2]

print(quadratic_equation_im(1,0,0))
print(quadratic_equation_im(1,0,2))
print(quadratic_equation_im(1,6,8))
