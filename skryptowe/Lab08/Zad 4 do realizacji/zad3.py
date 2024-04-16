# 3. Rozbudowujemy zadanie 1 dodatkwo zapisując w pliku score_3.txt tylko 3 najlepsze wyniki
# Występują w pliku tylko 3 wyniki. Jeśli na miejscu 3 i 4 wynik jest taki sam to zostawiamy wynik starszy.
# Przykładowa zawartość pliku result.txt (elementy rozdzielamy średnikiem):
# 1; Anna; 2023-11-22 13:23:23; Wyrzucono 6 i 6! po; 7; rzutach.
# 2; Mateusz; 2023-11-24 11:43:53; Wyrzucono 4 i 6! po; 12; rzutach.
# 3; Piotr; 2023-11-24 17:43:53; Wyrzucono 4 i 2! po; 23; rzutach.
import datetime
import os
from zad1 import Result, play, from_line


def parse_best():
    if os.path.exists("result.txt"):
        with open("result.txt","r") as file:
            return [from_line(line) for line in file]
    return []
def save_best(result:Result):
    results = parse_best()
    results.append(result)
    results.sort(key=lambda r: [r.tosses, r.date.timestamp() * -1 ])
    
    i = 1
    for res in results:
        res.position = i
        i += 1
    with open("result.txt","w") as file:
        [file.write(f"{res.display()}\n") for res in results if res.position <= 3]

res = play(6,6, "Anna")
save_best(res)

