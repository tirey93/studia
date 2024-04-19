# 3. Czytamy wszystkei dane z pliku cereals.csv (wykorzystać moduł csv)
# Dodajemy do pliku cereals.csv na końcu jednego wiersza z dowolnymi danymi.
# np. "Miodek","G ","C ",100,4,2,340,1,16,8,60,25,1,1,0.75,3.755922,1,0,0,0,1,0,0
from csv import  reader,writer

with open('cereals.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',', )
    headers = next(csv_reader)
    for row in csv_reader:
        print(row)
with open('cereals.csv', 'a+') as csv_file:
    csv_writer = writer(csv_file, delimiter=',', )
    csv_writer.writerow(["Miodek","G ","C ",100,4,2,340,1,16,8,60,25,1,1,0.75,3.755922,1,0,0,0,1,0,0])