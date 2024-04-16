# 4. Obliczanie BMI jako funkcja bmi(height, mass) zwraca informację
#    w postaci liczby BMI, a następnie funkcję bmi_opis(height, mass),
#    która zwraca opis słowny, niedowaga, waga poprawna
#    itd. wykorzystując w swoim ciele funkcję bmi(height, mass)

def bmi(height, mass):
    return mass/float(height*height);
def bmi_opis(height, mass):
    bmi_res = bmi(height, mass)
    if bmi_res < 18.5:
        return ('Niedowaga')
    if bmi_res >= 18.5 and bmi_res < 25:
        return("Pożądana masa ciała")
    if bmi_res >= 25 and bmi_res < 30:
        return('Nadwaga')
    if bmi_res >= 30:
        return('Otyłość')
print(bmi_opis(1.72, 66))