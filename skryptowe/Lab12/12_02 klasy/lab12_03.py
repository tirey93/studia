# 3. Zdefiniować klasę Calculator
# (Standardowy + - * / opcja zapamiętywania oraz kasowania wyniku)
# metody add(self, amount), subtract(self, amount), multiply(self, amount), division(self, amount).
# Gdzie amount wartość, która jest np. dodawana do wartości w pamięci current.

# Następnie zdefiniować klasę ScientificCalculator, która dziedziczy po klasie Calculator
# Zawiera metody pierwiastek_kwadratowy, zamiana radiany na kąty i odwrotnie oraz sin i cos

class Calculator():
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

if __name__=='__main__':
    c1 = Calculator()
    c1.add(2)
    print(c1.current)
    c1.add(3)
    print(c1.current)

    c2 = Calculator()
    c2.add(4)
    print(c2.current)
    c2.add(6)
    print(c2.current)
