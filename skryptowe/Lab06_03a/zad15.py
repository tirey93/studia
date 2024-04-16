# 15. Wyświetl kalendarz za rok 2022 i zobacz
# czy układ Świąt Bożego Narodzenia wygląda atrakcyjnie, czy nie
# (jeżeli święta są w tygodniu to OK, jeśli zahaczają o sobotę i niedzielę to Nie)
import calendar

print(calendar.month(2022,12))

# print(calendar.weekday(2022,12,24))
# print(calendar.weekday(2022,12,25))

if calendar.weekday(2022,12,24) in (5,6)\
        or calendar.weekday(2022,12,25) in (5,6):
    print("Nie")
else:
    print("Ok")