# 4. Zapisujemy do pliku kąt w stopniach, sinus i consinus z przedziału 0,360 co 1 stopień
# oraz czytamy dane z pliku o nazwie result_sin.tsv. Dane rozdzielamy tabulatorem \t
# Jeśli plik istnieje do kasujemy jego zawartość.
# Przy odczycie stosujemy różne sposoby formatowania łańcucha znaków ( %, .format() oraz f'),
# ale efekt wyświetlania danych ma być taki sam.
import math

with open("sin.tsv","w") as file:
    for i in range(360):
        file.write(f"{i}\t{math.sin(math.radians(i))}\n")