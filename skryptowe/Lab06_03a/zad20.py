# 20. Mamy teskt:
# dane = 'Litwo, Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, kto cię stracił. Dziś piękność twą w całej ozdobie widzę i opisuję, bo tęsknię po tobie'
# Policz: - ile jest spacji w danym tekście.
#         - ile jest znaków pisanych dużymi literami
#         - ile jest znaków pisanych dużymi literami.
#         - ile jest pozostałych znaków.
# Przekształć tekst na listę, gdzie separatorem elementu jest spacja.

dane = 'Litwo, Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, kto cię stracił. Dziś piękność twą w całej ozdobie widzę i opisuję, bo tęsknię po tobie'

spacje = 0
duze_litery = 0
male_litery = 0
pozostale = 0
for i in range(0, len(dane)):
    other = True
    if dane[i] == " ":
        spacje += 1
        other = False
    if dane[i].isupper():
        duze_litery += 1
        other = False
    if dane[i].islower():
        male_litery += 1
        other = False
    if other:
        pozostale += 1

print(f"Ile spacji: {spacje}")
print(f"Ile duzych liter: {duze_litery}")
print(f"Ile malych liter: {male_litery}")
print(f"Ile pozostalych znakow: {pozostale}")

print(dane.split(" "))


