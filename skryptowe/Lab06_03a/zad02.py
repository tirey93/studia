# 2. Dana jest lista:
# lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]
# Oblicz sumę, wartość średnią, wartość minimalną i maksymalną z wykorzystaniem
# i bez korzystania z funkcji wbudowanych sum, min, max, len.

lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]

print(sum(lista))
print(min(lista))
print(max(lista))
print(len(lista))
print()

def suma(arr):
    res = 0
    for i in arr:
        res += i
    return  res
def min1(arr):
    res = arr[0]
    for i in arr[1:]:
        if i < res:
            res = i
    return res
def max1(arr):
    res = arr[0]
    for i in arr[1:]:
        if i > res:
            res = i
    return res
def len1(arr):
    res = 0
    for i in arr:
        res += 1
    return res
print(suma(lista))
print(min1(lista))
print(max1(lista))
print(len1(lista))