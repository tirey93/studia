# 6. Liczenie wartości funkcji podanej z klawiatury np. (x*x+2x+4 lub 1/(x+1)) (wykorzystać funkcję eval())
# oraz zapisanie do pliku wzoru oraz wartości x, y dla 500 elementów od 0 do 50 o kroku 0.1.
# Jeżeli będzie dzielenie przez zero to należy obsłużyć błąd i zamknąć plik.

from csv import writer

equation = input("Podaj funkcje z parametrem 'x': ")

with open("function_6.csv","w", newline='', encoding='utf-8') as file:
    csv_writer = writer(file, delimiter=',')
    csv_writer.writerow(['x', 'y'])
    for i in range(50*10):
        x = i/10.0
        try:
            y = eval(equation)
        except ZeroDivisionError:
            break
        csv_writer.writerow([x, y])
        