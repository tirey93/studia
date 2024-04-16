# 7. Ile aktualnie lat ma Adam Małysz (albo dowolna osoba).
# Zdefiniuj funkcję how_old(date).
import datetime

def how_old(date):
    today = datetime.date.today()
    years = today.year - date.year
    if today.month < date.month or (today.month == date.month and today.day < date.day):
        years -= 1
    return years
now = datetime.date(2020,5,25)
print(how_old(now))