import neurolab as nl
# Program 1 – modelowanie działania perceptronu
#Zbiór uczący
train = [[0, 0], [0, 1], [1, 0], [1, 1]]
train_target = [[0], [0], [0], [1]]
#Zbiór testowy
test = [[2, 1], [2,2], [-1,0], [-1,1]]
test_targets=[[1], [1], [0], [0]]
#Tworzymy sieć z 2 wejściami i 1 neuronem
net = nl.net.newp([[-1, 2],[0, 2]], 1)

#Uczymy sieć
error = net.train(train, train_target, epochs=100, show=10, lr=0.1)
#Symulujemy
out = net.sim(test)
#Obliczamy błąd
f = nl.error.MSE()
test_error = f(test_targets, out)
print ("Błąd klasyfikacji: %f" %test_error)
print("Wzorzec",test_targets)
print("Wynik zwrócony przez SSN",out)
