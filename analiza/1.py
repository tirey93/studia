import random
import nltk


print()
def pobierz_cechy(imie):
    return {
        'pierwsza litera': imie[len(imie)//2]
    }

imiona_meskie = nltk.corpus.names.words('male.txt')
imiona_zenskie = nltk.corpus.names.words('female.txt')
oznaczone_imiona = [(imie, 'mezczyzna') for imie in imiona_meskie]
oznaczone_imiona += [(imie, 'kobieta') for imie in imiona_zenskie]

random.shuffle(oznaczone_imiona)
# print(oznaczone_imiona)

zestaw_cech = [(pobierz_cechy(imie), plec) for (imie, plec) in oznaczone_imiona]
# print(zestaw_cech)
zestaw_treningowy, zestaw_testowy = zestaw_cech[1000:], zestaw_cech[:1000]

bayes_klasyfikator = nltk.NaiveBayesClassifier.train(zestaw_treningowy)

# print(bayes_klasyfikator.classify(pobierz_cechy('Damian')))
print(nltk.classify.accuracy(bayes_klasyfikator, zestaw_testowy))

# bayes_klasyfikator.show_most_informative_features(10)

 