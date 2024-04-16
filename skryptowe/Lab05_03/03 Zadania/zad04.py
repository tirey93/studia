# 4. Dana jest lista (można dodać dowolną o dowolnej liczbie elementów):
# lista = [7, 13, 3, 6, 18, 6, 25, 5, 24, 4, 2, 4, 5, 3, ,1, 19, 71, 21]
# Znajdz wszystkie trzy kolejne liczby z listy, które są malejące.
# W naszym przypadku są następujące trójki liczby:
# 24, 4, 2
# 5, 3, ,1
# Jeżeli dana trójka liczba jest już wykorzystana,
# to idziemy dalej i dany element listy nie może być już wykorzystany
# np. lista = [5,4,3,2,1] to mamy tylko
# jedną trójkę liczb [5,4,3] - trójka liczb  [4,3,2] oraz [3,2,1] nie są rozwiązaniem.

lista = [7, 13, 3, 6, 18, 6, 25, 5, 24, 4, 2, 4, 5, 3 ,1, -1, -2, 21]
# lista = [5,4,3,2,1]
res = []

candidate = []
black_listed = []
last = lista[0]
candidate.append(last)

for i in range(1, len(lista) - 1):
    for j in range(2):
        if lista[i + j] < last and lista[i + j] not in black_listed:
            candidate.append(lista[i + j])
        last = lista[i + j]
    if len(candidate) == 3:
        res.append(candidate)
        [black_listed.append(x) for x in candidate]
    candidate = []
    last = lista[i]
    if last not in black_listed:
        candidate.append(last)
print(res)
