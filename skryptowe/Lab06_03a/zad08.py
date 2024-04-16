# 8. Podaj ile dni upłyneło od 1.01.2000 roku do aktualnej daty
import datetime

d0 = datetime.date(2000, 1, 1)
d1 = datetime.datetime.now().date()
diff = d1 - d0
print(diff.days)