# 1. Wyświetlamy, każdą kolumnę i wartości w kolumnie występujące w pliku california1.txt.
# Całość zapisujemy do pliku california.csv jako plik tekstowy z separatorem średnik ';'.
# Jaka jest populacja ludzi we wszystkich miastach w przedziale wieku 18 - 64 lata
# i jaki to procent wszystkich ludzi. Plik california1.txt jest taki sam jak pobrany w poprzednich zajęciach.

class California:
    place:str
    population:int
    pct_under_18:float
    pct_between_18_64:float
    pct_over_64:float
    ratio:float

    def display(self):
        return f"{self.place};{self.population};{self.pct_under_18};{self.pct_between_18_64};{self.pct_over_64};{self.ratio}\n"

def from_line(line:str):
    result = California()

    splitted = trim_line(line)
    result.place = splitted[0]
    result.population = int(splitted[1])
    result.pct_under_18 = float(splitted[2])
    result.pct_between_18_64 = float(splitted[3])
    result.pct_over_64 = float(splitted[4])
    result.ratio = float(splitted[5])

    return result

def trim_line(line:str):
    splitted = line.split("  ")
    return [x for x in splitted if len(x) > 0]

with open("california.txt","w") as file_w:
    whole_pop_18_64 = 0
    whole_pop = 0
    with open("california1.txt","r") as file_r:
        next(file_r)
        for line in file_r:
            cal = from_line(line)
            whole_pop += cal.population
            whole_pop_18_64 += cal.population * cal.pct_between_18_64
            file_w.write(cal.display())
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
    print(whole_pop)
    print(whole_pop_18_64 / whole_pop)

# line = "Los Angeles city                       3485398  24.8  65.3  10.0   99.6\n"
# # s = line.split("  ")
# # print(s)


# print(trim_line(line))