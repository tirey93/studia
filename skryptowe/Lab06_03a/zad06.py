# 6. Podaj, w jaki dzień tygodnia urodził się Adam Małysz.
# Data podana może być dowolna. Zdefiniuj funkcję.
import calendar
import datetime

def dayOfWeek(date):
    return calendar.day_name[date.weekday()]
now = datetime.datetime.now()
print(dayOfWeek(now))