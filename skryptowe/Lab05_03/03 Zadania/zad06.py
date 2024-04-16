# 6. Wykorzystaj moduł datetime do podania w osobnych linijkach
# roku, miesiąca, dnia oraz godziny, minuty i sekundy w danym momencie.

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)

