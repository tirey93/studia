import neurolab as nl
import numpy as np
import pylab as pl

def calculate_mse(target, output):
    return np.mean((np.array(target) - np.array(output)) ** 2)

def train_and_test_network(train_method, hidden_neurons, num_samples=30):
    x = np.linspace(-7, 7, num_samples)
    y1 = 2 * x * np.cos(x)
    wsp = np.abs(max(y1) - min(y1))
    y = y1 / wsp
    inp = x.reshape(num_samples, 1)
    tar = y.reshape(num_samples, 1)

    net = nl.net.newff([[-7, 7]], [hidden_neurons, 1])
    
    if train_method == "train_gd":
        net.trainf = nl.train.train_gd
    elif train_method == "train_gdm":
        net.trainf = nl.train.train_gdm
    elif train_method == "train_gda":
        net.trainf = nl.train.train_gda
    else:
        raise ValueError("Nieznana metoda treningu: " + train_method)


    error = net.train(inp, tar, epochs=1000, show=100, goal=0.01)
    out = net.sim(inp)
    mse = calculate_mse(tar, out)

    return mse, error[-1] #zwracamy MSE i ostatni błąd z train


train_methods = ["train_gd"]
hidden_neuron_counts = [3, 5, 10, 20, 30, 50]

results = {}

for train_method in train_methods:
    results[train_method] = {}
    print(f"Metoda treningu: {train_method}")
    for neurons in hidden_neuron_counts:
        mse, last_error = train_and_test_network(train_method, neurons)
        results[train_method][neurons] = {"mse": mse, "last_error": last_error}
        print(f"  Liczba neuronów: {neurons}, MSE: {mse:.4f}, Ostatni błąd: {last_error:.4f}")