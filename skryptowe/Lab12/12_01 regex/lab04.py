# Sprawdź ile wyrazów PYthon pisany dowolnymi literami jest w zdaniu
# Zamień wszystkie wystąpienia słowa python (podowlne litery) na słowo PYTHON
# pisany dużymi literami.
# Ile jest wyrazów rozdzielnych białymi znakami.
import re

zdanie = 'PYTHON. To jest kolokwium z przedmiotu Programowanie skryptowe, ' \
         'które wykorzystuje język python. PythoN jest OK, PythON'

wynik = re.findall('python', zdanie, re.IGNORECASE)
print(wynik)
print(wynik.__len__())
wynik1 = re.sub('python','PYTHON', zdanie, flags=re.IGNORECASE)
print(wynik1)

wynik2 = re.split("\s", zdanie)
print(wynik2.__len__())