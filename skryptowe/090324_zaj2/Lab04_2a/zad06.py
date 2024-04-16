# 6. Jaka to liczba? Komputer wybiera losowo liczbę z zakresu od 1 do 100.
#    Gracz próbuje ją odgadnąć, a komputer go informuje,
#    czy podana przez niego liczba jest:
#    za duża, za mała, prawidłowa
#    (na końcu podajemy ile liczb podaliśmy aby zgadnąć wylosowaną liczbę)
import random

draw = random.randint(1, 100)

count = 1
shot = int(input("Spróbuj odgadnąć liczbę: "))
while shot != draw:
    if shot > draw:
        print("Podana liczba jest za duża.")
    if shot < draw:
        print("Podana liczba jest za mała.")
    shot = int(input("Spróbuj odgadnąć liczbę: "))
    count += 1
print(f"Trafiłeś za {count} razem")