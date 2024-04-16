# 16. Do bieżącej daty dadaj 3 tygodnie lub 21 dni (datetime.timedelta(...))
import datetime

now = datetime.datetime.now().date()
print(now)

print(now + datetime.timedelta(days=21))
print(now + datetime.timedelta(weeks=3))