# 3. Zdefiniować klasę Calculator
# (Standardowy + - * / opcja zapamiętywania oraz kasowania wyniku)
# metody add(self, amount), subtract(self, amount), multiply(self, amount), division(self, amount).
# Gdzie amount wartość, która jest np. dodawana do wartości w pamięci current.

# Następnie zdefiniować klasę ScientificCalculator, która dziedziczy po klasie Calculator
# Zawiera metody pierwiastek_kwadratowy, zamiana radiany na kąty i odwrotnie oraz sin i cos


import math


class Calculator():
    def __init__(self):
        self.current = 0

    def remove(self):
        self.saved = 0
    
    def save(self):
        self.saved = self.current

    def add(self, amount):
        self.current += amount

    def subtract(self, amount):
        self.current -= amount

    def multiply(self, amount):
        self.current *= amount

    def division(self, amount):
        if amount != 0:
            self.current /= amount
        else:
            print("Dzielenie przez zero!")

class ScientificCalculator(Calculator):
    def square(self):
        self.current= pow(self.current, 0.5)
    def rad_to_deg(self):
        self.current = math.degrees(self.current)
    def deg_to_rad(self):
        self.current = math.radians(self.current)
    def sin(self):
        self.current = math.sin(self.current)
    def cos(self):
        self.current = math.cos(self.current)

if __name__=='__main__':
    c2 = Calculator()
    c2.add(4)
    print(c2.current)
    c2.add(6)
    print(c2.current)
    c2.subtract(2)
    print(c2.current)
    c2.multiply(3)
    print(c2.current)
    c2.division(2)
    print(c2.current)

    print()
    sc = ScientificCalculator()
    sc.add(9)
    print(sc.current)
    sc.square()
    print(sc.current)