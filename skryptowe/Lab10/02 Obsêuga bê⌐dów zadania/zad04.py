# Napisz przykładowy kod z obsługą błędów przy odwoływaniu się do indeksu listy poza zakresem

list = [1,5,16,45]

try:
    value = list[5]
    print(value)
except:
    print("Element doesn't exists")