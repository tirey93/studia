# 10. Rzucamy dwoma kośćmi wielokrotnie, aż wyrzucimy dokładnie sumę zdaną np. 100.
#     Jeśli suma wyrzucona w poprzednim rzucie jest za duża w stosunku do zadanej sumy to odejmujemy dany rzut 
#     a jak wynik jest mniejszy od zadanej sumy to dodajemy wartości wyrzucone do  aktualnej sumy oczek.
#     Rejestrujemy wszystkie wyrzucone wartości i ich aktualną sumę (funkcja print()).
#     Na końcu podajemy ile rzutów wykonaliśmy, aby osiągnąć wartość zadaną np. 100.
import random

goal = 100
sum = 0
count = 1

while sum != goal:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    throw = dice1 + dice2
    print(f"Suma: {sum}, kość1: {dice1}, kość2: {dice2}")
    if sum < goal:
        sum += throw
    elif sum > goal:
        sum -= throw
    count += 1
print(f"Ilosc rzutow: {count}")