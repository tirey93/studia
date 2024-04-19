# 0. (zadanie z ostatnich zajęć)
# - nie kopiujemy pliku do danego katalogu, tylko próbujemy otworzyć plik z katalogu Lab08/....)
# Mamy plik tekstowy z danymi medycznymi msk_impact_2017_clinical_data.tsv
# Należy podać ile jest w danym pliku linii,
# Następnie ile jest kobiet i mężyczyzn
# (sprawdzić czy istnieją rekordy, gdzie nie pojawia się informacja jaka jest płeć - wypisać te wartości lub rekordy)
# Podać ilość precentowy kobiet i mężczyzn w tej populacji.

with open("../Lab08/Zad 4 do realizacji/msk_impact_2017_clinical_data.tsv","r") as file:
    i = 0
    female_count = 0
    male_count = 0
    next(file)
    for line in file:
        i += 1
        values = line.split("\t")
        match values[19]:
            case "Female": female_count += 1
            case "Male": male_count += 1
            case _: print(line)

print(i)
print(female_count)
print(female_count * 100 / i)
print(male_count)
print(male_count * 100 / i)

        
        
        