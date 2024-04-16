# app06
# - Wyświetlamy liczby od 10 do 0 w jednej linijce a przy liczbie 3 wychodzimy z pętli (konstrukcja while oraz instrukcją break)
i = 10
while i >0:
    # print(f"i: {i}")
    if i == 3:
        break
    i -= 1
# - Wykonujemy to samo co wyżej tylko konstrukcja while ma na stałe postać - while True: (zawsze prawda)
print('\n')
i = 10
while True:
    # print(f"i: {i}")
    if i <= 0 or i == 3:
        break
    i -= 1
# - Wyświetlamy liczby od 100 do 90 w jednej linijce a przy liczbie 95 i 93 pomijamy wyświetlanie (konstrukcja while oraz instrukcją continue (bez break))
i = 101
while i > 90:
    i -= 1
    if i == 95 or i == 93:
        continue
    # print(i)
# - Wykonujemy to samo co wyżej tylko konstrukcja while ma na stałe postać - while True: (zawsze prawda) (z instrukcją continue i break)
i = 101
while True:
    i -= 1
    if i == 95 or i == 93:
        continue;
    if i < 90:
        break;
    print(i)















