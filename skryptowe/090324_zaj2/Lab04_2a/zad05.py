# 5. Losujemy liczby od 1-100 i po ilu losowaniach suma wyrzuconych wartości
#    tylko liczb parzystych będzie nie większa od wartości podanej jako parametr funkcji
#    count_random_even_numbers(sum_max).
import random


def count_random_even_numbers(sum_max):
    suma = 0
    count = 0
    while suma <= sum_max:
        draw = random.randint(0,100)
        # print(f"count: {count}, suma: {suma}, draw: {draw}")
        if draw % 2 == 0:
            suma += draw
            count += 1
    return count
count_random_even_numbers(233)