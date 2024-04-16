# 3. Dana jest lista (można dodać dowolną o dowolnej liczbie elementów):
# lista = [7, 13, 3, 6, 18, 6, 25, 5, 24, 4, 2, 4, 5, 3, ,1, -1, -2, 21]
# Znajdz wszystkie (łącznie z wykorzystanymi wcześniej) trzy kolejne liczby z listy,
# które są malejące.
# Dany element listy może być ponownie wykorzystany.
# np. lista = [5,4,3,2,1] to mamy tutaj trzy trójki liczb [5,4,3], [4,3,2] oraz [3,2,1], które są rozwiązaniem.

lista = [7, 13, 3, 6, 18, 6, 25, 5, 24, 4, 2, 4, 5, 3 ,1, -1, -2, 21]
# lista = [5,4,3,2,1]
res = []

candidate = []
last = lista[0]
candidate.append(last)

for i in range(1, len(lista) - 1):
    for j in range(2):
        if lista[i + j] < last:
            candidate.append(lista[i + j])
        last = lista[i + j]
    if len(candidate) == 3:
        res.append(candidate)
    candidate = []
    last = lista[i]
    candidate.append(last)
print(res)
