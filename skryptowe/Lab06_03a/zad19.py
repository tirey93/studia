# 19. Dana jest lista składająca się z liczb całkowitych:
# dane = [7, 3, 3, 9, 18, 6, 5, 24, 24, 4, 4, 5, 3, 7, 3, 24]
# Należy wyeliminować powtarzające się wartości w danej liście i posortować malejąco.
# (program ma działać dla dowolnej liczby składającej się z liczb całkowitych)

dane = [7, 3, 3, 9, 18, 6, 5, 24, 24, 4, 4, 5, 3, 7, 3, 24]

non_dupl = []
for i in dane:
    if i not  in non_dupl:
        non_dupl.append(i)

dane = non_dupl

print(sorted(dane, reverse=True))
