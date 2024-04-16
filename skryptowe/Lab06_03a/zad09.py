# 9. Zapropnuj słownik lub listę do sprawdzenia oceny w zależności od liczby punktów
# podanej z klawiatury (do wyboru oceny od 2-5 stosujemy słownik lub listę)
# Jeżeli zmienią się zakresy na liście lub oceny to także wynik końcowy może być inny.
# 	5 - (80%-100%>
# 	4 - (60%-80%>
# 	3 - (50-60%>
# 	2 - <=50%>

oceny = {
    5: [80, 100],
    4: [60, 80],
    3: [50, 60],
    2: [0, 50],
}

def jaka_ocena(punkty, oceny):
    for ocena in oceny:
        range = oceny[ocena]
        if punkty > range[0] and punkty <= range[1]:
            return  ocena
print(jaka_ocena(65, oceny))

