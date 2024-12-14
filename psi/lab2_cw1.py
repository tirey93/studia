

import numpy as np

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def train_network(P, T, W, n_epochs, learning_rate=0.1):
  print()
  print()
  num_inputs = P.shape[0]
  num_outputs = T.shape[0]
  num_samples = P.shape[1]

  for epoch in range(n_epochs):
    sample_order = np.random.permutation(num_samples)

    for i in sample_order:
      p = P[:, i].reshape(num_inputs, 1)
      t = T[:, i].reshape(num_outputs, 1)

      a = sigmoid(W[:, i] @ p)

      e = t[i] - a

      W[:, i] += learning_rate * e.T

  return W

# Dane wejściowe i wyjściowe
P = np.array([
    [4.0000, 2.0000, -1.0000],
    [0.0100, -1.0000, 3.5000],
    [0.0100, 2.0000, 0.0100],
    [-1.0000, 2.5000, -2.0000],
    [-1.5000, 2.0000, 1.5000]
])

T = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Wagi początkowe
Wprzed = np.random.uniform(low=-0.5, high=0.5, size=(5, 3))

# Liczba epok
n_epochs = 1000

# Trenowanie sieci
W_trained = train_network(P, T, Wprzed.copy(), n_epochs)

print(W_trained)

# Testowanie sieci na danych wejściowych
print("\nTestowanie sieci:")
for i in range(P.shape[1]):
    p = P[:, i].reshape(P.shape[0],1)
    a = sigmoid(W_trained[:, i] @ p)
    print(f"Wejście: {p.flatten()}, Wyjście sieci: {a.flatten()}, Oczekiwane wyjście: {T[:,i]}")

print("\nNowy test:")
t_new = np.array([
    [6.0000],
    [0.0200],
    [0.0200],
    [-2.0000],
    [-2.5000]
])
for i in range(P.shape[1]):
    p = t_new[:, 0].reshape(P.shape[0],1)
    a = sigmoid(W_trained[:, i] @ p)
    print(f"Wejście: {p.flatten()}, Wyjście sieci: {a.flatten()}, Oczekiwane wyjście: {T[:,i]}")