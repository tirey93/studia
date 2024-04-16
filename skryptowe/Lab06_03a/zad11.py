# 11. Pobierz od użytkownika n liczb i zapisz je na liście.
# Wydrukuj: elementy listy i ich indeksy (enumerate),
# elementy w odwrotnej kolejności, posortowane elementy.
# Usuń z listy pierwsze wystąpienie elementu podanego przez użytkownika.
# Usuń z listy element o podanym indeksie.
# Podaj ilość wystąpień oraz indeks pierwszego wystąpienia podanego elementu.
# Wybierz z listy elementy od indeksu i do j.

# lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 16, 256, 3, 19, 71, 21]
n = int(input("Podaj ile liczb zamierzasz wpisac: "))
lista = []
for i in range(n):
    element = int(input(f"Podaj {i + 1} element: "))
    lista.append(element)

print("Wydrukuj: elementy listy i ich indeksy (enumerate)")
for i in range(len(lista)):
    print(f"{i} - {lista[i]}")

print("elementy w odwrotnej kolejności,")
for i in range(len(lista)-1, -1, -1):
    print(f"{i} - {lista[i]}")

# posortowane elementy.
print("posortowane elementy.")
sorted = sorted(lista)
for i in range(len(sorted)):
    print(f"{i} - {sorted[i]}")

print("Usuń z listy pierwsze wystąpienie elementu podanego przez użytkownika.")
def usunZList1(lista:list, doUsuniecia:int):
    res = []
    alreadyDeleted = False
    for x in lista:
        if x != doUsuniecia or alreadyDeleted:
           res.append(x)
        else:
            alreadyDeleted = True;
    return res
print(usunZList1(lista, 3))

print("Usuń z listy element o podanym indeksie.")
def usunZList2(lista:list, doUsuniecia:int):
    return [x for x in lista if x != doUsuniecia]
print(usunZList2(lista, 3))

print("Podaj ilość wystąpień")
def ileWystapien(lista:list, element:int):
    return len([x for x in lista if x == element])

print(f"{ileWystapien(lista, 3)}")
print("indeks pierwszego wystąpienia podanego elementu.")
def pierwszeWystapienie(lista:list, element:int):
    for i in range(len(lista)):
        if lista[i] == element:
           return i;
print(f"{pierwszeWystapienie(lista, 3)}")

print("Wybierz z listy elementy od indeksu i do j.")
def zakresListy(lista:list, i:int, j:int):
    return [lista[x] for x in range(i, j)]
print(zakresListy(lista, 2, 6))