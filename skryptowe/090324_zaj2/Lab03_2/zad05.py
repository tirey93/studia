# 5. Sprawdź czy podana liczba jest liczbą pierwszą i zdefiniuj funkcję is_prime(a) zwracjącą wartość True lub False. 
#    - wymyślamy swój algorytm niekoniecznie optymalny 
#    - (2 jest liczbą pierwszą, liczby mniejsze od 2 nie są liczbami pierwszymi, liczby większe od 2 - zależy od liczby)
import math


def isPrimeNumber(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

print(isPrimeNumber(53))
print(isPrimeNumber(35))
print(isPrimeNumber(555))
print(isPrimeNumber(557))