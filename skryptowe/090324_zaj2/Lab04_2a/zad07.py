# 7. Podajemy funkcję (na stałe w programie)
# np. liniową (y=x-1), kwadratową (y=3*x**2+7*x-19), hiberbolę(y=1/x+5)
# i sprawdzamy jej wartość w pkt. podanym z klawiatury 
# (nie obsługujemy błędów nawet jeśli będzie dzielenie przez zero)

def liniowa(x):
    return x - 1
def kwadratowa(x):
    return 3*x**2+7*x-19
def hiperbola(x):
    return 1/x+5

# print(liniowa(34))
# print(kwadratowa(34))
# print(hiperbola(34))
# print(liniowa(-34))
# print(kwadratowa(-34))
# print(hiperbola(-34))
# print(liniowa(0))
# print(kwadratowa(0))

x = float(input("Podaj x: "))
print(liniowa(x))
print(kwadratowa(x))
print(hiperbola(x))