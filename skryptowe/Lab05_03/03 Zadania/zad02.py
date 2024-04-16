# 2. Uzupełnij listę do 10 adresów i posortuj ją rosnąco po nazwie.
# Listę uzupełniamy z klawiatury i spradzamy ile jest elementów listy.
# Nie dodajemy adresu, który już istnieje.
# data = ['user3@gmail.com','user2@gmail.com','user2@interia.com','user1@gmail.com','user1@interia.com']
# W ramach tej samej listy wybierz do losowania tylko adresy z poczty gmail.com i posortuj ją rosnąco po nazwie.

data = ['user3@gmail.com','user2@gmail.com','user2@interia.com','user1@gmail.com','user1@interia.com']

while (len(data) < 10):
    email = input("Podaj adres email: ")
    if email not in data:
        data.append(email)
d1 = [mail for mail in data if "@gmail.com" in mail]
print(d1)