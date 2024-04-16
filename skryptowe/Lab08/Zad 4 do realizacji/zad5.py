# 5. Czytanie danych z internetu z pliku tekstowego (wykorzystać moduł urllib.request)
# i wyświetlamy w programie tylko pierwszych 10 linii.
# Plik znajduje się w lokalizacji (jeśli nie można odnaleźć tego pliku to poszukać inny plik w prtalu kaggle.com):
# https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv

# Dodatkowo proszę poszukać plik w sieci o adresie
# 'https://imsi.p.lodz.pl/o-instytucie/pracownicy-instytutu'
# i znaleźć w nim string 'Dyrekcja Instytutu Mechatroniki i Systemów Informatycznych' i wyświetlić cały wiersz z tym stringiem.

import http.client
from urllib import request

r:http.client.HTTPResponse = request.urlopen("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv")

#print(r.read().decode(r.info().get_param('charset') or 'utf-8'))
lines = r.readlines()
# print(lines[:10])

r2:http.client.HTTPResponse = request.urlopen("https://imsi.p.lodz.pl/o-instytucie/pracownicy-instytutu")

lines2 = r2.readlines()
print([line.decode('utf-8') for line in lines2 if b'Dyrekcja Instytutu Mechatroniki' in line])