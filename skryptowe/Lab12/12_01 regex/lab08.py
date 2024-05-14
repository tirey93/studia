# Napisz wyrażenie regularne do sprawdzenia czy podany czas
# w formacie hh:min:sec.100sec jest poprawny (tylko pełne dopasowanie)
import re

time = "04:12:59.789"
match = re.fullmatch("[0-2][0-9]:[0-5][0-9]:[0-5][0-9].[0-9][0-9][0-9]", time)
print(match)