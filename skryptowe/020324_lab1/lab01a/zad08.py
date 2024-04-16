# app08
# Rzucamy czterema kośćmi aż wyrzucimy cztery szóstki lub cztery jedynki 
# jednocześnie liczymy ile razy losowaliśmy aby zaistniała taka sytuacja.
# Wyświetlamy tylko ilość rzutów oraz informację czy wyrzuculiśmy jedynki czy szóstki
import random

skucha6 = True
skucha1 = True
n = 1
while skucha6 and skucha1:
    skucha6 = False
    skucha1 = False
    for i in range(4):
        rzut = random.randrange(6)
        # print(rzut, end=" ")
        if rzut != 5 and not skucha6:
            skucha6 = True
        if rzut != 0 and not skucha1:
            skucha1 = True
        if skucha1 and skucha6:
            break
    n += 1
    # print()
if skucha1:
    odpowiedz = "jedynki"
else:
    odpowiedz = "szostki"
print(f"Ilosc losowan: {n}, wylosowano 4 {odpowiedz}")
# Modyfikujemy naszą aplikację aby można rzucać maksymalnie 100 kośćmi - podawanych z klawiatury.

skucha6 = True
skucha1 = True
iloscKosci = int(input("Podaj ilosc kosci: "))
if iloscKosci > 100:
    print("Za duzo kosci!")
    exit()
n = 1
while skucha6 and skucha1:
    skucha6 = False
    skucha1 = False
    for i in range(iloscKosci):
        rzut = random.randrange(6)
        # print(rzut, end=" ")
        if rzut != 5 and not skucha6:
            skucha6 = True
        if rzut != 0 and not skucha1:
            skucha1 = True
        if skucha1 and skucha6:
            break
    n += 1
    # print()
if skucha1:
    odpowiedz = "jedynki"
else:
    odpowiedz = "szostki"
print(f"Ilosc losowan: {n}, wylosowano {iloscKosci} razy {odpowiedz}")