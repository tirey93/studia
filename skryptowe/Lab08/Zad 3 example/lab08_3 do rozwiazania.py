# 8.3. Dla pliku dane.dat obliczyć sumaryczny czas ruchu,
# sumaryczną przebytą drogę oraz prędkość średnią.

results = []
with open("dane.dat","r") as file:
    results = [[float(val) for val in line.split()]
     for line in file if line[0] != "#"]

print(f"suma ruch: {sum([x[0] for x in results])}")
print(f"suma droga: {sum([x[1] for x in results])}")
print(f"predkosc srednia: {sum([x[2] for x in results])*1.0 / len([x[2] for x in results])}")