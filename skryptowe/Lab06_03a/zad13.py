# 13. Zmień sposób wyświetlenia daty tak, aby niedziela była pierwszym dniem
# tygodnia (calendar.setfirstweekday(6))
# i ponownie wyświetl miesiąc z ważną dla Ciebie datą
import calendar
import datetime

calendar.setfirstweekday(6)

print(calendar.month(2020,1))