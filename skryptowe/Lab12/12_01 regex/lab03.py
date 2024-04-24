# Sprawdź ile adresów email jest poprawnych i wyświetl w postaci listy, które są poprawne
import re

email = 'a1_f@wp.pl, a1_f@wp.pl, a3@wp.pl'

wynik = re.findall(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}', email, re.IGNORECASE)

if wynik:
    print('ok')
    print(wynik)
    print(len(wynik))
else:
    print('No')