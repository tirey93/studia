# 5. Wykorzystaj moduł datetime do podania w jednej linijce
#   rok-miesiąc-dzień oraz godzina:minuty:sekundy
#   w danym momencie z wykorzystaniem najnowszego formatowania danych f-string (f').
import datetime

now = datetime.datetime.now()

print(f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}")