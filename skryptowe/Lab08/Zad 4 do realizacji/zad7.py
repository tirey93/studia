# 7. Mamy plik tekstowy z danymi medycznymi msk_impact_2017_clinical_data.tsv
# Należy podać ile jest w danym pliku linii (wierszy bez wiersza nagłówkowego).
# Następnie wyświetlić te wiersze, które mają największą liczbę znaków z wyłączeniem białych znaków.

def count_characters_in_string(mystring):
    return sum(not c.isspace() for c in mystring)

with open("msk_impact_2017_clinical_data.tsv","r") as file:
    i = 0
    max = 0
    lines = []
    next(file)
    for line in file:
        i += 1
        count = count_characters_in_string(line)
        if max < count:
            max = count
            lines = []
        if max == count:
            lines.append(line)

    print(i)
    print(len(lines))
    for line in lines:
        print(f"{len(line)}\t{line}")