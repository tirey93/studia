# Napisz przykładowy kod z obsługą błędów przy podawaniu błędnej daty z klawiatury
# (ponawiamy podawanie daty, aż bedzie poprawna).
import datetime

date = input("Enter date: ")
isError = True
while isError:
    try:
        date_type = datetime.datetime.strptime(date, "%Y-%m-%d")
        isError = False
    except:
        print("Incorrect date. Please try again.")
        date = input("Enter date: ")